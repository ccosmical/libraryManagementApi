from rest_framework.serializers import ModelSerializer

from .models import library_management

class library_managementSerializer(ModelSerializer):
    class Meta:

        model= library_management
        fields = ('title','author','publication_date','ISBN','category','number_of_pages')