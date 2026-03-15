from .models import Course
from .serializers import CourseSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from modular_entity_mapping_system.utils import get_object
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class CourseListCreateView(APIView):
    """
    List all courses and create new course
    """
    
    @swagger_auto_schema(responses={200:CourseSerializer(many=True)})
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True) 
        return Response(serializer.data,status=status.HTTP_200_OK)    
    
    
    @swagger_auto_schema(
        request_body=CourseSerializer,
        responses={201:CourseSerializer})
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CourseDetailView(APIView):
    """
    Retrieve, update, delete a course
    """
    
    @swagger_auto_schema(responses={200:CourseSerializer})
    def get(self,request,pk):
        course = get_object(Course,pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(
        request_body=CourseSerializer,
        responses={200:CourseSerializer})
    def put(self,request,pk):
        course = get_object(Course,pk)
        serializer = CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema(
        request_body=CourseSerializer,
        responses={200:CourseSerializer})
    def patch(self,request,pk):
        course = get_object(Course,pk)
        serializer = CourseSerializer(course,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema(responses={204:"No Content"})
    def delete(self,request,pk):
        course = get_object(Course,pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        