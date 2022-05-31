from rest_framework import viewsets
from .serializers import CategorySerializer
from ..models import ProductCategory

# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer