from django.db import models

# Create your models here.

class library_management(models.Model):
    title=models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    ISBN=models.CharField()
    category = models.TextField()
    number_of_pages=models.CharField(max_length=10)

    def __str__(self):
        return self.title
