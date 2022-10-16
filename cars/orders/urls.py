from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from .views import view_orders
from .api import CarColorViewSet, CarBrandViewSet, CarModelViewSet, OrderViewSet, \
    OrderColorCountViewSet, OrderBrandCountViewSet


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

router = DefaultRouter()

router.register('order/color_count', OrderColorCountViewSet)
router.register('order/brand_count', OrderBrandCountViewSet)
router.register('order', OrderViewSet)
router.register('color', CarColorViewSet)
router.register('brand', CarBrandViewSet)
router.register('model', CarModelViewSet)


urlpatterns = [
    path('api/', include([
        path('', include(router.urls)),
        path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    ])
         ),
    path('', view_orders, name='orders'),
]

