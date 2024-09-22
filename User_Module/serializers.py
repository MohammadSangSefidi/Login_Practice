from rest_framework import serializers
from User_Module.models import UserModel


class LoginSerializer(serializers.Serializer):
    """
        The Login serializer for validate login request
    """

    username = serializers.CharField(max_length=255, required=True, write_only=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)

    class Meta:
        fields = ['username', 'password']