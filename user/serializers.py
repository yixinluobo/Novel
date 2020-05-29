import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        field = ['username', 'password', 'email', 'mobile']
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
            }
        }

    def validate_username(self, value):
        '''验证用户名是否存在'''
        user = models.User.objects.get(username=value)
        if user is not None:
            raise ValidationError("该用户名已存在")
        return value

    def validate_email(self, value):
        '''验证邮箱格式'''
        is_vali_email = re.compile('\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}')
        if is_vali_email.match(value):
            return value
        raise ValidationError('邮箱格式不正确')

