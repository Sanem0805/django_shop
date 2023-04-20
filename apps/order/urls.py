from rest_framework import routers

from .views import OrderViewSet

routers = routers.DefaultRouter()
routers.register('oreder', OrderViewSet, 'order')

urlpatterns = routers.urls