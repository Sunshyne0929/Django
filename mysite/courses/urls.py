from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='courses_index'),
    path('detail/', views.detail, name='course_detail'),
    path('instructors/', views.instructors, name='course_instructors'),
]
