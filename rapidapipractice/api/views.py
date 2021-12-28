from django.contrib.auth.models import Group, User
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import UserSerializer,GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializers_class = GroupSerializer