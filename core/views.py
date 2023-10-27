from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,  UpdateView, CreateView, DeleteView, DetailView
from .models import *
from .forms import *


class AlunoView(TemplateView):
    template_name = "aluno.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alunos"] = Aluno.objects.all()
        return context
    

class EditAlunoView(UpdateView):
    model = Aluno
    form_class = AlunoForm  
    template_name = "edit_aluno.html"
    success_url = '/alunos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["aluno"] = self.get_object() 
        return context

class CreateAlunoView(CreateView):
    model = Aluno
    form_class = AlunoForm 
    template_name = "create_aluno.html"  
    success_url = '/alunos/'  

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteAlunoView(DeleteView):
    model = Aluno
    template_name = "delete_aluno.html" 
    success_url = reverse_lazy('aluno') 

    def get_object(self, queryset=None):
        return Aluno.objects.get(pk=self.kwargs['pk'])

class AlunoDetailView(DetailView):
    model = Aluno
    template_name = "detail_aluno.html" 
    context_object_name = "aluno" 