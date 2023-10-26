from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,  UpdateView, CreateView, DeleteView, DetailView
from .models import *
from .forms import *


class StudentView(TemplateView):
    template_name = "student.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()
        return context
    

class EditStudentView(UpdateView):
    model = Student
    form_class = StudentForm  
    template_name = "edit_students.html"
    success_url = '/alunos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student"] = self.get_object() 
        return context

class CreateStudentView(CreateView):
    model = Student
    form_class = StudentForm 
    template_name = "create_student.html"  
    success_url = '/alunos/'  

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteStudentView(DeleteView):
    model = Student
    template_name = "delete_student.html" 
    success_url = reverse_lazy('student') 

    def get_object(self, queryset=None):
        return Student.objects.get(pk=self.kwargs['pk'])

class StudentDetailView(DetailView):
    model = Student
    template_name = "detail_student.html" 
    context_object_name = "student" 