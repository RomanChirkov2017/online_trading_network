from django.contrib.auth import login
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView,
                                     UpdateAPIView)

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, LoginSerializer


class UserCreateAPIView(CreateAPIView):
    """
    View-класс для создания нового пользователя.
    Наследуется от класса CreateAPIView из модуля rest_framework.generics.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    """
    View-класс для получения списка всех пользователей.
    Наследуется от класса ListAPIView из модуля rest_framework.generics.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    """
    View-класс для изменения информации о пользователе.
    Наследуется от класса UpdateAPIView из модуля rest_framework.generics.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(DestroyAPIView):
    """
    View-класс для удаления пользователя.
    Наследуется от класса DestroyAPIView из модуля rest_framework.generics.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class LoginView(CreateAPIView):
    """
    View-класс для аутентификации пользователя.
    Наследуется от класса CreateAPIView из модуля rest_framework.generics.
    """

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)


