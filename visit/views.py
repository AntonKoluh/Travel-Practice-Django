from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serializer import VisitSerializer
from .models import Visit
from project.pagination import StandardResultsSetPagination


class PlaceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "place_id",
        "is_visited",
    ]

    search_fields = [
        "place_id",
        "is_visited",
    ]

    ordering_fields = [
        "id",
        "is_visited",
        "place_id",
    ]

    ordering = ["id"]

    def get_queryset(self):
        queryset = Visit.objects.all()

        incoming_project_id = self.request.query_params.get("project_id")

        if incoming_project_id:
            queryset = queryset.filter(project_id=incoming_project_id)

        return queryset

    def partial_update(self, request, *args, **kwargs):
        allowed_field = {"notes", "is_visited"}

        invalid_fields = set(request.data.keys()) - allowed_field

        if invalid_fields:
            raise ValidationError(
                {
                    "detail": f"PATCH can only update {', '.join(allowed_field)}",
                    "invalid_fields": list(invalid_fields),
                }
            )

        return super().partial_update(request, *args, **kwargs)
