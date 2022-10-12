from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Order


def index(request):
    return redirect('orders')


def view_orders(request):
    orders = Order.objects.all()
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'car_orders/orders.html', {'page_obj': page_obj})



