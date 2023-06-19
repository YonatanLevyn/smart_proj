from rest_framework import serializers
from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer): 
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_by', 'created_at', 'updated_at']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'youtube_video_id', 'course', 'created_at', 'updated_at']