from django.shortcuts import render
from .models import Course
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

def say_hello(request):
    return render(request, template_name = 'index.html')

def course_list_view(request):
    all_courses = Course.objects.all()
    data = {'courses': all_courses}
    return render(request, template_name ='index.html', context=data)

class CourseListView(ListView):
    model = Course
    template_name = 'course_list_view.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail_view.html'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'course_create_view.html'
    fields = '__all__'
    success_url = '/all-courses'

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_update_view.html'
    fields = '__all__'
    success_url = '/all-courses'


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_delete_view.html'
    success_url = '/all-courses'