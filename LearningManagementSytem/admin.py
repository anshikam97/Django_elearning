from django.contrib import admin
from instructor.models import *

@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
