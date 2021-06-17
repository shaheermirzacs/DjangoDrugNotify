# serializers.py

from rest_framework import serializers
from rest_framework import validators
from rest_framework.validators import UniqueTogetherValidator
from .models import User, Test
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    date_checked = serializers.DateField(
        format='%Y-%m-%d',
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Test
        fields = '__all__'