from django.contrib import admin

from .models import CarColor, CarBrand, CarModel, Order


class CarColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color')
    list_display_links = ('id', 'color',)
    search_fields = ('id', 'color',)


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand')
    list_display_links = ('id', 'brand',)
    search_fields = ('id', 'brand',)


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_model', 'brand')
    list_display_links = ('id', 'car_model',)
    search_fields = ('id', 'car_model',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'color', 'car_model', 'count', 'date')
    list_display_links = ('order_number', 'car_model',)
    search_fields = ('order_number', 'car_model',)


admin.site.register(CarColor, CarColorAdmin)
admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Order, OrderAdmin)
