"""
URL configuration for education project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from course.views import (CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('all-courses/', CourseListView.as_view()),
    path('course/<int:pk>', CourseDetailView.as_view()),
    path('create-course/', CourseCreateView.as_view()),
    path('update-course/<int:pk>', CourseUpdateView.as_view()),
    path('delete-course/<int:pk>', CourseDeleteView.as_view())
]
