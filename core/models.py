from django.db import models

class Cidade(models.Model):
    name = models.CharField("Nome", max_length=100)
    state = models.CharField("Estado", max_length=2)
    def __str__(self):
        return self.name

class Cursos(models.Model):
    name = models.CharField("Nome", max_length=100)

    class Meta:
        
        verbose_name_plural = 'Cursos'
    def __str__(self):
        return self.name
    
class Aluno(models.Model):
    name = models.CharField("Nome", max_length=100)
    address = models.CharField("Endereço", max_length=100)
    email = models.EmailField("E-mail", max_length=100)
    date_of_birth = models.DateField("Data de Nascimento")
    city = models.ForeignKey(Cidade, on_delete=models.CASCADE)  
    course = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
