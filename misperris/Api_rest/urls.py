from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from .views import HuerfanosViewSet

routers = routers.DefaultRouter()
routers.register(r'huerfanos', HuerfanosViewSet)

urlpatterns = [
    path(r'', include(routers.urls)),
    path(r'api-url', include('rest_framework.urls', namespace='rest_framework'))
]
