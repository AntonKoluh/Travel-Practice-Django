from rest_framework import serializers
from .models import Visit
from .services.validate_external_id import check_external_api


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ["place_id", "project", "is_visited", "notes"]

    def validate(self, attrs):
        qs = Visit.objects.filter(project=attrs.get("project")).count()

        if qs >= 10:
            raise serializers.ValidationError("Cannot have over 10 places per project")

        return attrs

    def validate_place_id(self, value):
        check, respose = check_external_api(value)

        if check is False:
            raise serializers.ValidationError(respose)

        return value
