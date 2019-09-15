from rest_framework import serializers
from django.contrib.auth.models import User

from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username',)


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields = ('employee', 'date_from', 'date_to', 'status', 'reason', 'time_received', 'time_approved')
