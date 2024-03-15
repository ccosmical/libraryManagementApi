from django.shortcuts import render
from .models import library_management
from .serializer import library_managementSerializer
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from permissions import isAuthenticatedOrReadOnly


# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([isAuthenticatedOrReadOnly])
def library_management_list(request):
    if request.method == 'GET':
        #creating pagination object and settings
        paginator=PageNumberPagination()
        paginator.page_size=10

        #creating filter object and setting search fields
        search_fields= ['title','author','publication_date','category']
        filter_backend = SearchFilter(search_fields=search_fields)
        
        library = library_management.objects.all()
        
        result_page = paginator.paginate_queryset(library, request)
        serializer = library_managementSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        library = library_management.objects.all()
        serializer = library_managementSerializer(library, many=True)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([isAuthenticatedOrReadOnly])
def library_management_detail(request, pk):
    try:
        instance = library_management.objects.get(pk=pk)
    except library_management.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == "GET":
        paginator = PageNumberPagination()
        paginator.page_size=10

        search_fields=['title','author','publication_date','category']
        filter_backend= SearchFilter(search_fields)

        result_page = paginator.paginate_queryset(instance, request)
        serializer = library_managementSerializer(result_page)
        return paginator.get_paginated_response(serializer)
    
    elif request.method == "PUT":
        serializer = library_managementSerializer(library_management, request=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        instance.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
        