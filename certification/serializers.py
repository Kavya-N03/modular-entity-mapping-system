from .models import Certification
from rest_framework import serializers

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = [
            "id",
            "name",
            "code",
            "description",
            "is_active",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["created_at","updated_at"]