from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from modular_entity_mapping_system.utils import get_object
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.
class VendorProductMappingListCreateView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "vendor_id",
                openapi.IN_QUERY,
                description="Filter mappings by vendor_id",
                type=openapi.TYPE_INTEGER
            )
        ],
        responses={200:VendorProductMappingSerializer(many=True)}
    )
    def get(self,request):
        vendor_id = request.query_params.get("vendor_id")
        vendor_mapping = VendorProductMapping.objects.all()
        if vendor_id:
            vendor_mapping = vendor_mapping.filter(vendor_id=vendor_id)
        
        serializer = VendorProductMappingSerializer(vendor_mapping,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(
        request_body=VendorProductMappingSerializer,
        responses={201:VendorProductMappingSerializer})
    def post(self,request):
        serializer = VendorProductMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class VendorProductMappingDetailView(APIView):
    
    @swagger_auto_schema(responses={200:VendorProductMappingSerializer})
    def get(self,request,pk):
        vendor_mapping = get_object(VendorProductMapping,pk)
        serializer = VendorProductMappingSerializer(vendor_mapping)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(
        request_body=VendorProductMappingSerializer,
        responses={200:VendorProductMappingSerializer})
    def put(self,request,pk):
        vendor_mapping = get_object(VendorProductMapping,pk)
        serializer = VendorProductMappingSerializer(vendor_mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema(
        request_body=VendorProductMappingSerializer,
        responses={200:VendorProductMappingSerializer})
    def patch(self,request,pk):
        vendor_mapping = get_object(VendorProductMapping,pk)
        serializer = VendorProductMappingSerializer(vendor_mapping,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema({200:"Mapping Deactivated"})
    def delete(self,request,pk):
        """Soft delete using is_active=False."""
        vendor_mapping = get_object(VendorProductMapping,pk)
        if not vendor_mapping.is_active:
            return Response({
                "message":"Vendor mapping is already inactive"
            })
        vendor_mapping.is_active = False
        vendor_mapping.save()
        return Response({
            "message":"Vendor mapping deactivated successfully."
        },status=status.HTTP_200_OK)