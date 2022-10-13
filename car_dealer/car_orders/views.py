from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Order
from .forms import CheckBoxTrueForm, CheckBoxFalseForm, BrandsForm


SORTED_COUNT = None
PAGE_NUMBER = None


def index(request):
    return redirect('orders')


def view_orders(request):
    global SORTED_COUNT, PAGE_NUMBER
    if request.method == 'POST':
        url = request.get_full_path()
        if 'sorted_count' in request.POST and request.POST['sorted_count']:
            SORTED_COUNT = True
        else:
            SORTED_COUNT = False
        if PAGE_NUMBER:
            url += f'?page={PAGE_NUMBER}'
        return redirect(url)

    elif request.method == 'GET':
        context = {}
        if SORTED_COUNT:
            form = CheckBoxTrueForm()
            orders = Order.objects.all().order_by('count')
        else:
            form = CheckBoxFalseForm()
            orders = Order.objects.all()
        form_brands = BrandsForm()
        context['form'] = form
        context['form_brands'] = form_brands
        print(form_brands.as_ul())
        paginator = Paginator(orders, 10)
        page_number = request.GET.get('page')
        PAGE_NUMBER = page_number
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['paginator'] = paginator
        return render(request, 'car_orders/orders.html', context=context)
