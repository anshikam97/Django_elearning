from django.db import models
from LearningManagementSytem.models import UserProfile, Category, SubCategory
from instructor.models import Courses

class Cart(models.Model):
	class Meta():
		unique_together = ('course', 'user')
		
	course = models.ForeignKey(Courses, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Orders(models.Model):
    order_id = models.CharField(max_length=100, unique=True, default="")
    order_date = models.DateTimeField(auto_now=True)
    total_amt = models.DecimalField(decimal_places=2, max_digits=30)
    paid_by = models.CharField(max_length=20, default="Debit")
    placed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="") 

class Opted(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    added_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    dated = models.DateTimeField(auto_now=True)