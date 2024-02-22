from django.shortcuts import render
from .models import library_management
from .serializer import library_managementSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def library_list(request):

    if request == "GET":