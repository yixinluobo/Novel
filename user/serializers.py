from rest_framework import serializers
from user import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'required': '必填项',
                    'min_length': '密码强度太低',
                    'max_length': '密码长度过长',
                }
            },
            'username': {
                'required': True,
                'error_messages': {
                    'required': '必填项',
                }
            },
            'is_superuser': {
                'write_only': True,
            },
            'is_staff': {
                'write_only': True,
            },
            'is_active': {
                'write_only': True,
            },
            'first_name': {
                'write_only': True,
            },
            'last_name': {
                'write_only': True,
            },
            'date_joined': {
                'write_only': True,
            },
            'groups': {
                'write_only': True,
            },
            'user_permissions': {
                'write_only': True,
            },
        }
