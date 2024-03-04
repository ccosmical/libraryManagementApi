from django.shortcuts import render
from .models import library_management
from .serializer import library_managementSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', 'POST'])
def library_management_list(request):
    if request.method == 'GET':
        library = library_management.objects.all()
        serializer = library_managementSerializer(library, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        library = library_management.objects.all()
        serializer = library_managementSerializer(library, many=True)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def library_management_detail(request, pk):
    try:
        instance = library_management.objects.get(pk=pk)
    except library_management.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == "GET":
        serializer = library_managementSerializer(instance)
        return Response(serializer)
    
    elif request.method == "PUT":
        serializer = library_managementSerializer(library_management, request=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        instance.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
        