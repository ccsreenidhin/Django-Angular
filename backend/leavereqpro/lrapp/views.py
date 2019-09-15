from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from rest_framework import generics

from . import models
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ApplicationListView(generics.ListAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer


class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer


class ApplicationCreate(generics.ListCreateAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

    def perform_create(self, serializer):
        serializer.status = 'processing'
        serializer.save()
