from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from modular_entity_mapping_system.utils import get_object
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class CourseCertificationMappingView(APIView):
    """
    List all course_certification_mapping and create new course_certification_mapping
    """
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'course_id',
                openapi.IN_QUERY,
                description="Filter mappings by course_id",
                type=openapi.TYPE_INTEGER
            )
        ],
        responses={200:CourseCertificationMappingSerializer(many=True)}
    )
    def get(self,request):
        course_id = request.query_params.get("course_id")
        
        course_mapping = CourseCertificationMapping.objects.all()
        if course_id:
            course_mapping = course_mapping.filter(course_id=course_id)
        serializer = CourseCertificationMappingSerializer(course_mapping, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(
        request_body=CourseCertificationMappingSerializer,
        responses={201:CourseCertificationMappingSerializer})
    def post(self,request):
        serializer = CourseCertificationMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CourseCertificationMappingDetailView(APIView):
    """
    Retrieve, update,delete a course_certificate_mapping
    """
    
    @swagger_auto_schema(responses={200:CourseCertificationMappingSerializer})
    def get(self,request,pk):
        course_mapping = get_object(CourseCertificationMapping,pk)
        serializer = CourseCertificationMappingSerializer(course_mapping)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
    @swagger_auto_schema(
        request_body=CourseCertificationMappingSerializer,
        responses={200:CourseCertificationMappingSerializer})
    def put(self,request,pk):
        course_mapping = get_object(CourseCertificationMapping,pk)
        serializer = CourseCertificationMappingSerializer(course_mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema(
        request_body=CourseCertificationMappingSerializer,
        responses={200:CourseCertificationMappingSerializer})
    def patch(self,request,pk):
        course_mapping = get_object(CourseCertificationMapping,pk)
        serializer = CourseCertificationMappingSerializer(course_mapping,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

    @swagger_auto_schema(responses={200:"Mapping Deactivated"})
    def delete(self,request,pk):
        """ Soft delete using is_active=False. """
        
        course_mapping = get_object(CourseCertificationMapping,pk)
        if not course_mapping.is_active:
            return Response({
                "message":"Course Mapping is already inactive"
            })
        course_mapping.is_active = False
        course_mapping.save()
        return Response({
            "message":"Course Mapping deactivated successfully."
        },status=status.HTTP_200_OK)
