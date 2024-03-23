from rest_framework.test import APITestCase
from rest_framework import status
from .models import library_management
from .serializer import library_managementSerializer
from django.urls import reverse

# Create your tests here.

class library_managementAPITestCase(APITestCase):
    
    def setUp(self):    
        self.book = library_management.objects.create(title= 'Test Book', author= 'Test Author')
       

    def test_get_book_list(self):
        url = reverse('library_management_list')
        response= self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_create_book(self):
        url=reverse('library_management_list')
        data = {'title':'New Book', 'author':'New Author'}
        response= self.client.post(url, data)
       
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_update_book(self):
        url= reverse('library_management_detail', kwargs={'pk': self.book.pk})
        data = {'title': 'Updated Title', 'author': 'Updated Author'}
        response= self.client.put(url,data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title,'Updated Title')


    def test_delete_book(self):
        url = reverse('library_management_detail', kwargs= {'pk': self.book.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)
        self.assertFalse(library_management.objects.filter(pk=self.book.pk).exists())