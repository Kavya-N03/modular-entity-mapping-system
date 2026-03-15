from rest_framework import serializers
from .models import VendorProductMapping
from vendor.serializers import VendorSerializer
from product.serializers import ProductSerializer


class VendorProductMappingSerializer(serializers.ModelSerializer):

    vendor_details = VendorSerializer(source="vendor", read_only=True)
    product_details = ProductSerializer(source="product", read_only=True)

    class Meta:
        model = VendorProductMapping
        fields = [
            "id",
            "vendor",
            "vendor_details",
            "product",
            "product_details",
            "primary_mapping",
            "is_active",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["created_at","updated_at"]

    def validate(self, data):
        vendor = data.get("vendor", getattr(self.instance, "vendor", None))
        primary = data.get("primary_mapping", getattr(self.instance, "primary_mapping", False))
        
        if primary:
            queryset = VendorProductMapping.objects.filter(
                vendor=vendor,
                primary_mapping=True
            )

            if self.instance:
                queryset = queryset.exclude(id=self.instance.id)

            if queryset.exists():
                raise serializers.ValidationError({
                    "primary_mapping": "This vendor already has a primary mapping."
                })

        return data