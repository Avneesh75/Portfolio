from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    subject=models.CharField(max_length=50)
    message=models.TextField(max_length=100)
