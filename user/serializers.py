from rest_framework import serializers
from django.contrib.auth.models import User



"""Class user to serializer a user model."""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']