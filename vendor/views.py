from .models import Vendor
from .serializers import VendorSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from modular_entity_mapping_system.utils import get_object
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class VendorListCreateView(APIView):
    """
    List all Vendors and Create new vendor
    """
    
    @swagger_auto_schema(responses={200:VendorSerializer(many=True)})
    def get(self,request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=VendorSerializer,
        responses={201:VendorSerializer}
    )
    def post(self,request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class VendorDetailView(APIView):
    """
    Retrive, update, delete a vendor
    """
    
    @swagger_auto_schema(responses={200:VendorSerializer})
    def get(self,request,pk):
        vendor = get_object(Vendor,pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    
    @swagger_auto_schema(
        request_body=VendorSerializer,
        responses={200:VendorSerializer}
    )
    def put(self,request,pk):
        vendor = get_object(Vendor,pk)
        serializer = VendorSerializer(vendor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        request_body=VendorSerializer,
        responses={200:VendorSerializer}
    )
    def patch(self,request,pk):
        vendor = get_object(Vendor,pk)
        serializer = VendorSerializer(vendor,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    @swagger_auto_schema(responses={204:"No Content"})
    def delete(self,request,pk):
        vendor = get_object(Vendor,pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)