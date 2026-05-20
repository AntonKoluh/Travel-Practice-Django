from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializer import ProjectSerializer
from .models import Projects
from .pagination import StandardResultsSetPagination


class ProjectsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "name",
        "start_date",
    ]

    search_fields = [
        "name",
        "description",
    ]

    ordering_fields = [
        "id",
        "name",
        "start_date",
    ]

    ordering = ["id"]
