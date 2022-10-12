from django.urls import path

from .views import view_orders


urlpatterns = [
    path('', view_orders, name='orders'),
]
