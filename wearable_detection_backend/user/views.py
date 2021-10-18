from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User


@api_view(['POST'])
def register(request):
    '''
    用户注册
    :param request: data域包括username,phone,password,sex,birthday
    :return: -1:昵称已被注册， -2：手机已被注册，0：注册成功
    '''
    if request.method == 'POST':
        username = request.data.get('username')
        phone = request.data.get('phone')
        password = request.data.get('password')
        sex = request.data.get('sex')
        birthday = request.data.get('birthday')

        if User.objects.filter(Q(username=username)).exists():
            # 昵称已被注册
            return Response(-1, status=status.HTTP_200_OK)
        if User.objects.filter(Q(phone=phone)).exists():
            # 手机已被注册
            return Response(-2, status=status.HTTP_200_OK)

        user = User()
        user.username = username
        user.phone = phone
        user.password = password
        user.sex = sex
        user.birthday = birthday
        user.save()

        # 注册成功
        return Response(0, status=status.HTTP_200_OK)
