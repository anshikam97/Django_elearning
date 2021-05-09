from django.db import models
from LearningManagementSytem.models import UserProfile, Category, SubCategory

class Courses(models.Model):

    STATUS = (
        ('A', 'Accept'),
        ('R', 'Reject'),
    )

    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    course_img = models.ImageField(upload_to="course_image", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    level = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    added_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    dated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, choices=STATUS)


class Lecture(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    dated = models.DateTimeField(auto_now=True)
    video = models.FileField(upload_to='course_lecture_videos/')

