from django.urls import include,path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
routers.register(r'users', views.UserViewSet)
routers.register(r'users', views.GroupViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', name='rest_framework'))
]
