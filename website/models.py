from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='proyectos',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo
