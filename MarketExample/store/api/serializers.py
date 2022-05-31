from rest_framework import serializers
from ..models import ProductCategory


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'name', 
            'slug'
        ]

