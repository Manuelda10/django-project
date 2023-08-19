from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, 'products')
router.register(r'categories', views.CategoryViewSet, 'categories')

urlpatterns = [
    path('', include(router.urls))
]

