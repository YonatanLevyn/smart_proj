from django.db import models

class PageView(models.Model):
    url = models.CharField(max_length=255)  # Stores the visited URL as a string
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically sets the timestamp to the current time when a new instance is created

    def __str__(self):
        return f"{self.url} - {self.timestamp}"  # Human-readable representation of the model
