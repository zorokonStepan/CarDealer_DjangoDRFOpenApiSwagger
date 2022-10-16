from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Order, CarModel, CarBrand
from .forms import BrandsForm, CheckBoxForm


SORTED_COUNT = None
PAGE_NUMBER = None
BRAND = None


def index(request):
    return redirect('orders')


def view_orders(request):
    global SORTED_COUNT, PAGE_NUMBER, BRAND

    if request.method == 'POST':
        if 'sorted_count' in request.POST and request.POST['sorted_count']:
            SORTED_COUNT = True
        else:
            SORTED_COUNT = None

        url = request.get_full_path()
        if PAGE_NUMBER:
            url += f'?page={PAGE_NUMBER}'

        if 'brand' in request.POST:
            BRAND = request.POST.getlist('brand')
        else:
            BRAND = None

        return redirect(url)

    elif request.method == 'GET':
        context = {}
        # create forms and get data from databases
        form = CheckBoxForm()
        if SORTED_COUNT:
            form.fields['sorted_count'].initial = True

        form_brands = BrandsForm()
        if BRAND:
            form_brands.fields['brand'].initial = BRAND
            brands = CarBrand.objects.filter(id__in=BRAND)
            car_models = CarModel.objects.filter(brand__in=brands)
            if SORTED_COUNT:
                orders = Order.objects.filter(car_model__in=car_models).order_by('count')
            else:
                orders = Order.objects.filter(car_model__in=car_models)
        else:
            orders = Order.objects.all()
        # pagination
        paginator = Paginator(orders, 10)
        page_number = request.GET.get('page')
        PAGE_NUMBER = page_number
        page_obj = paginator.get_page(page_number)
        # create context
        context['form'] = form
        context['form_brands'] = form_brands
        context['page_obj'] = page_obj
        context['paginator'] = paginator

        return render(request, 'orders/orders.html', context=context)
