from django.db import models

# Create your models here.
class Proyecto(models.Model):
	descripcion=models.CharField(max_length=512)
	cliente=models.CharField(max_length=30)
	fecha_limite=models.DateField()

class Grupo(models.Model):
	nombre=models.CharField(max_length=30)
	proyecto=models.OneToOneField(Proyecto, on_delete=models.CASCADE)

class Estudiante(models.Model):
	nombre=models.CharField(max_length=30)
	correo=models.EmailField(max_length=256)
	numero=models.IntegerField()
	grupo=models.ForeignKey(Grupo, on_delete=models.CASCADE)

class Desafio(models.Model):
	titulo=models.CharField(max_length=30)
	descripcion=models.CharField(max_length=512)
	fecha=models.DateField()

class DesafiosEstudiantes(models.Model):
	estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
	desafio=models.ForeignKey(Desafio, on_delete=models.CASCADE)
	fueEntregado=models.BooleanField(default=False)