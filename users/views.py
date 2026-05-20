from rest_framework import viewsets
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
