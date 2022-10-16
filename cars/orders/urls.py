from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import view_orders
from .api import CarColorViewSet, CarBrandViewSet, CarModelViewSet, OrderViewSet, \
    OrderColorCountViewSet, OrderBrandCountViewSet


router = DefaultRouter()

router.register('order/color_count', OrderColorCountViewSet)
router.register('order/brand_count', OrderBrandCountViewSet)
router.register('order', OrderViewSet)
router.register('color', CarColorViewSet)
router.register('brand', CarBrandViewSet)
router.register('model', CarModelViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', view_orders, name='orders'),
]
