from django.urls import path
from .views import *
urlpatterns = [
    path("alunos/", StudentView.as_view(), name="student"),
    path("edit-student/<int:pk>", EditStudentView.as_view(), name="edit_student"),
    path('criar-aluno/', CreateStudentView.as_view(), name='criar_aluno'),
    path('excluir-aluno/<int:pk>/', DeleteStudentView.as_view(), name='excluir_aluno'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='detalhes_aluno'),
]
    