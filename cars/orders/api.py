from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Sum, Q

from .models import CarColor, CarBrand, CarModel, Order
from .serializers import CarColorSerializer, CarBrandSerializer, CarModelSerializer, OrderSerializer, \
    OrderGETSerializer, OrderColorCountSerializer, OrderBrandCountSerializer


class CarColorViewSet(viewsets.ModelViewSet):
    """
    Implements API CRUD
    To process a GET request with and without parameters, the method has been redefined list
    """
    queryset = CarColor.objects.all()
    serializer_class = CarColorSerializer


class CarBrandViewSet(viewsets.ModelViewSet):
    """
    Implements API CRUD
    To process a GET request with and without parameters, the method has been redefined list
    """
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    """
    Implements API CRUD
    To process a GET request with and without parameters, the method has been redefined list
    """
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = CarModel.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        data = request.data
        data['brand'] = CarBrand.objects.get(brand=data['brand']).id

        serializer = CarModelSerializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"patch": serializer.data})


class OrderViewSet(viewsets.ModelViewSet):
    """Implements API CRUD To process a GET request with and without parameters, the method has been redefined list"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        """To process a GET request with and without parameters"""
        queryset = Order.objects.all().values()
        for q in queryset:
            car_model = CarModel.objects.get(id=q['car_model_id'])
            q['car_model'] = car_model
            q['brand'] = car_model.brand
            q['color'] = CarColor.objects.get(id=q['color_id'])

        serializer_class = OrderGETSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Order.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        data = request.data
        _ = data.pop('brand', None)
        data['color'] = CarColor.objects.get(color=data['color']).id
        data['car_model'] = CarModel.objects.get(car_model=data['car_model']).id

        serializer = OrderSerializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"patch": serializer.data})


class OrderColorCountViewSet(viewsets.ModelViewSet):
    """Implements API CRUD To process a GET request with and without parameters, the method has been redefined list"""
    queryset = Order.objects.all()

    def list(self, request):
        """To process a GET request with and without parameters"""
        colors = CarColor.objects.all()
        queryset = []
        for color in colors:
            cnt = Order.objects.aggregate(sum=Sum('count', filter=Q(color=color)))['sum']
            if cnt:
                queryset.append({
                    'color': color,
                    'count': cnt
                })

        serializer_class = OrderColorCountSerializer(queryset, many=True)
        return Response(serializer_class.data)


class OrderBrandCountViewSet(viewsets.ModelViewSet):
    """Implements API CRUD To process a GET request with and without parameters, the method has been redefined list"""
    queryset = Order.objects.all()

    def list(self, request):
        """To process a GET request with and without parameters"""
        brands = CarBrand.objects.all()

        queryset = []

        for brand in brands:
            cnt = Order.objects.aggregate(sum=Sum('count', filter=Q(car_model__brand=brand.id)))['sum']
            if cnt:
                queryset.append({
                    'brand': brand,
                    'count': cnt
                })

        serializer_class = OrderBrandCountSerializer(queryset, many=True)
        return Response(serializer_class.data)




