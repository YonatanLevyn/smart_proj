from django.db import models
from django.conf import settings
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    ## get_absolute_url() method to return the URL of the created object
    def get_absolute_url(self):
        return reverse('courses:course_detail', args=[str(self.id)])


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)  
    youtube_video_id = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson_detail', args=[str(self.pk)])


