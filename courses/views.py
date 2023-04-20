from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from .models import Course, Lesson
from .utils import get_youtube_video_info
from django.shortcuts import get_object_or_404
from .forms import LessonForm
from django.urls import reverse
from django.urls import reverse_lazy

# CourseListView displays a list of all courses in the database
class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

    # Customize the context data to include the related lessons
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.object)
        return context


class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'description']
    template_name = 'courses/course_create.html'

    # Set the creator of the course to the current user
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CourseDeleteView(generic.DeleteView):
    model = Course
    template_name = 'courses/course_delete.html'
    success_url = reverse_lazy('courses:course_list')


# including the YouTube video information
class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'courses/lesson_detail.html'

    # Customize the context data to include the video information
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video_info = get_youtube_video_info(self.object.youtube_video_id)
        context['video_info'] = video_info
        return context

class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'courses/lesson_create.html'

    # Set the related course for the lesson
    def form_valid(self, form):
        course = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        form.instance.course = course
        return super().form_valid(form)

    # Redirect to the course detail page after successfully creating a lesson
    def get_success_url(self):
        return reverse('courses:course_detail', kwargs={'pk': self.object.course.pk})


class LessonDeleteView(generic.DeleteView):
    model = Lesson
    template_name = 'courses/lesson_delete.html'

    def get_success_url(self):
        return reverse('courses:course_detail', kwargs={'pk': self.object.course.pk})
