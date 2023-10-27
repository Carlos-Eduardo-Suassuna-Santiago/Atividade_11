from django.urls import path
from .views import *
urlpatterns = [
    path("alunos/", AlunoView.as_view(), name="aluno"),
    path("edit-aluno/<int:pk>", EditAlunoView.as_view(), name="edit_aluno"),
    path('criar-aluno/', CreateAlunoView.as_view(), name='criar_aluno'),
    path('excluir-aluno/<int:pk>/', DeleteAlunoView.as_view(), name='excluir_aluno'),
    path('Aluno/<int:pk>/', AlunoDetailView.as_view(), name='detalhes_aluno'),
]
    