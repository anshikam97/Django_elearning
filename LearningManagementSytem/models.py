from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    mobile = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100, unique=True)

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    message = models.CharField(max_length=500)