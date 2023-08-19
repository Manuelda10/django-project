from rest_framework import viewsets
from . import models, serializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ProductSerializer
    queryset = models.Product.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.CategorySerializer
    queryset = models.Category.objects.all()