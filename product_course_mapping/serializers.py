from .models import ProductCourseMapping
from rest_framework import serializers
from product.serializers import ProductSerializer
from course.serializers import CourseSerializer

class ProductCourseMappingSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source="product",read_only=True)
    course_details = CourseSerializer(source="course",read_only=True)
    
    class Meta:
        model = ProductCourseMapping
        fields = [
            "id",
            "product",
            "course",
            "product_details",
            "course_details",
            "primary_mapping",
            "is_active",
            "created_at",
            "updated_at"
            ]
        read_only_fields = ["created_at","updated_at"]
        
    def validate(self,data):
        product = data.get("product",getattr(self.instance,"product",None))
        primary = data.get("primary_mapping",getattr(self.instance,"primary_mapping",False))
            
        if primary:
            queryset = ProductCourseMapping.objects.filter(
                product=product,
                primary_mapping=True
                )
            if self.instance:
                    queryset = queryset.exclude(id=self.instance.id)
                
            if queryset.exists():
                    raise serializers.ValidationError({
                        "product":"This product already has a primary mapping."
                    })
            
        return data        
