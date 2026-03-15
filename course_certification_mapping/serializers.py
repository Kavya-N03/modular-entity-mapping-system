from .models import CourseCertificationMapping
from rest_framework import serializers
from course.serializers import CourseSerializer
from certification.serializers import CertificationSerializer

class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    course_details = CourseSerializer(source="course",read_only=True)
    certification_details = CertificationSerializer(source="certification",read_only=True)
    class Meta:
        model = CourseCertificationMapping
        fields = [
            "id",
            "course",
            "certification",
            "course_details",
            "certification_details",
            "primary_mapping",
            "is_active",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["created_at","updated_at"]
    
    def validate(self,data):
        course = data.get("course",getattr(self.instance,"course",None))
        primary = data.get("primary_mapping",getattr(self.instance,"primary_mapping",False))
        
        if primary:
            queryset = CourseCertificationMapping.objects.filter(
                course=course,
                primary_mapping = True
            )
            if self.instance:
                queryset = queryset.exclude(id=self.instance.id)
            
            if queryset.exists():
                raise serializers.ValidationError({
                    "course":"This course already has a primary mapping."
                })
                
        return data