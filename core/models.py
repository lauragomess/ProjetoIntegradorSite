from django.utils import timezone
from django.db import models
from .validators import validate_file_extension
from .choices import *
from django.contrib.auth.models import User

# Create your models here.
class Aluno(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		limit_choices_to={'groups__name': "Alunos"},
		related_name='aluno')
	cpf = models.CharField("CPF",max_length=11, null = True, blank = True)
	
	def __str__(self):              
		return self.user.first_name


class Tcc(models.Model):
	nome = models.CharField("Nome", max_length=120)
	aluno = models.ManyToManyField("Aluno")
	curso = models.IntegerField(choices=MY_CHOICES)
	document = models.FileField(upload_to='documents/',validators=[validate_file_extension], null = True, blank = True)


	def __str__(self):              
		return self.nome

	class Meta:
		 ordering = ('nome',)
