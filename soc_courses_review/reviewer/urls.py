from django.urls import path
from reviewer import views
app_name = 'reviewer'

urlpatterns = [
    path('', views.index, name='index'),
    path('AllCourses/', views.AllCourses, name='AllCourses'),
    path('Course/<slug:course_name_slug>/',
        views.show_course, name='show_course'),
]