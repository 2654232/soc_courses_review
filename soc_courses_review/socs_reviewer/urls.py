from django.urls import path
from socs_reviewer import views

app_name = 'socs_reviewer'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]