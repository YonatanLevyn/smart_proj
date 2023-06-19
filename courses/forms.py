from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'youtube_video_id']
    def clean_youtube_video_id(self):
        youtube_video_id = self.cleaned_data['youtube_video_id']
        if len(youtube_video_id) != 11:
            raise forms.ValidationError('Invalid YouTube video ID')
        return youtube_video_id
