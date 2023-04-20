from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<int:course_pk>/create_lesson/', views.LessonCreateView.as_view(), name='lesson_create'),
    path('<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('<int:course_pk>/<int:pk>/delete/', views.LessonDeleteView.as_view(), name='lesson_delete'),
    path('<int:course_pk>/<int:pk>/', views.LessonDetailView.as_view(), name='lesson_detail'),
]
