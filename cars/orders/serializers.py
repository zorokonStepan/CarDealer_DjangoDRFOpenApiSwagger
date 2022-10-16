import datetime
from rest_framework import serializers

from .models import CarColor, CarBrand, CarModel, Order


class CarColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarColor
        fields = ('id', 'color')


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('id', 'brand')


class CarModelSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(max_length=25)

    class Meta:
        model = CarModel
        fields = ('id', 'car_model', 'brand')

    def create(self, validated_data):
        validated_data['brand'] = CarBrand.objects.get(brand=validated_data['brand'])
        return CarModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'brand' in validated_data:
            validated_data['brand'] = CarBrand.objects.get(brand=validated_data['brand'])

        instance.car_model = validated_data.get("car_model", instance.car_model)
        instance.count = validated_data.get("brand", instance.brand)
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    color = serializers.CharField(max_length=50)
    car_model = serializers.CharField(max_length=25)

    class Meta:
        model = Order
        fields = ('order_number', 'date', 'color', 'car_model', 'count')

    def create(self, validated_data):
        _ = validated_data.pop('brand', None)
        if 'date' not in validated_data:
            validated_data['date'] = datetime.date.today().strftime('%Y-%m-%d')
        validated_data['color'] = CarColor.objects.get(color=validated_data['color'])
        validated_data['car_model'] = CarModel.objects.get(car_model=validated_data['car_model'])
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'color' in validated_data:
            validated_data['color'] = CarColor.objects.get(color=validated_data['color'])
        if 'car_model' in validated_data:
            validated_data['car_model'] = CarModel.objects.get(car_model=validated_data['car_model'])

        instance.date = validated_data.get("date", instance.date)
        instance.color = validated_data.get("color", instance.color)
        instance.car_model = validated_data.get("car_model", instance.car_model)
        instance.count = validated_data.get("count", instance.count)
        instance.save()
        return instance


class OrderGETSerializer(serializers.Serializer):
    date = serializers.DateField()
    color = serializers.CharField(max_length=50)
    car_model = serializers.CharField(max_length=25)
    brand = serializers.CharField(max_length=25)
    count = serializers.IntegerField()


class OrderColorCountSerializer(OrderGETSerializer):
    date = None
    car_model = None
    brand = None


class OrderBrandCountSerializer(OrderGETSerializer):
    date = None
    color = None
    car_model = None
