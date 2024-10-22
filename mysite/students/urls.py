from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='students_index'),
    path('profile/', views.profile, name='student_profile'),
    path('contact/', views.contact, name='student_contact'),
    path('home/', views.home, name='home'),  # Add home URL
]
