from django.shortcuts import render
from .serializers import UserRegisterSerializer, UserListSerializer
from rest_framework import generics
from .models import CustomUser
from rest_framework import permissions


# Create your views here.
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

