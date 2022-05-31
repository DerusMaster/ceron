from django.urls import path, include
from .views import CategoryViewSet
from rest_framework import routers
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
app_name = "api_store"

urlpatterns = [
    path('', include(router.urls)),
]