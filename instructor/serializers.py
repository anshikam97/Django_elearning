from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only = True)
    class Meta:
        model = Lecture
        fields = '__all__'



