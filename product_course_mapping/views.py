from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from modular_entity_mapping_system.utils import get_object
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class ProductCourseMappingListCreateView(APIView):
    """
    List all product_course_mapping and create new product_course_mapping
    """
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'product_id',
                openapi.IN_QUERY,
                description="Filter mappings by product_id",
                type=openapi.TYPE_INTEGER
            )
        ],
        responses={200:ProductCourseMappingSerializer(many=True)}
    )
    def get(self,request):
        product_id = request.query_params.get("product_id")
        
        product_mapping = ProductCourseMapping.objects.all()
        if product_id:
            product_mapping = product_mapping.filter(product_id=product_id)
            
        serializer = ProductCourseMappingSerializer(product_mapping,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(
        request_body=ProductCourseMappingSerializer,
        responses={201:ProductCourseMappingSerializer}
    )
    def post(self,request):
        serializer = ProductCourseMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class ProductCourseMappingDetailView(APIView):
    """
    Retrieve, update,delete a product_course_mapping
    """
    
    @swagger_auto_schema(responses={200:ProductCourseMappingSerializer})
    def get(self,request,pk):
        product_mapping = get_object(ProductCourseMapping,pk)
        serializer = ProductCourseMappingSerializer(product_mapping)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(
        request_body=ProductCourseMappingSerializer,
        responses={200:ProductCourseMappingSerializer}
    )
    def put(self,request,pk):
        product_mapping = get_object(ProductCourseMapping,pk)
        serializer = ProductCourseMappingSerializer(product_mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=ProductCourseMappingSerializer,
        responses={200:ProductCourseMappingSerializer}
    )
    def patch(self,request,pk):
        product_mapping = get_object(ProductCourseMapping,pk)
        serializer = ProductCourseMappingSerializer(product_mapping,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema(responses={200:"Mapping Deactivated"})
    def delete(self,request,pk):
        
        """Soft delete using is_active=False."""
        product_mapping = get_object(ProductCourseMapping,pk)
        if not product_mapping.is_active:
            return Response({
                "message":"Product mapping is already deactivated."
            })
        product_mapping.is_active = False
        product_mapping.save()
        return Response({
            "message":"Mapping deactivated successfully"
        },status=status.HTTP_200_OK)