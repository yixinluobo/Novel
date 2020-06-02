from datetime import datetime
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from user import serializers, models
from utils.response import APIResponse

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegisterAPIView(APIView):
    # 取消认证
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        data_ser = serializers.UserSerializer(data=request.data)
        data_ser.is_valid(raise_exception=True)
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        params = dict()
        params.setdefault('username', username)
        params.setdefault('password', password)
        params.setdefault('email', email)
        params.setdefault('mobile', mobile)
        params.setdefault('last_login', None)
        params.setdefault('is_superuser', 0)
        params.setdefault('first_name', '')
        params.setdefault('last_name', '')
        params.setdefault('is_staff', 1)
        params.setdefault('is_active', 1)
        params.setdefault('date_joined', datetime.now())

        user = models.User.objects.create(**params)
        user_ser = serializers.UserSerializer(user)
        return APIResponse(data_msg='注册成功！', results=user_ser.data)


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.User.objects.filter(username=username, password=password).first()
        if user is None:
            return APIResponse(data_status=1, data_msg='用户名或密码不存在')
        user_ser = serializers.UserSerializer(user)
        # 签发Token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return APIResponse(data_msg='登录成功', results=user_ser.data, token=token)





