from django.db import models

class Pokemon(models.Model):
    nombre=models.CharField(max_length=100, null=False)
    tipo=models.CharField(max_length=40, null=False)
    peso=models.IntegerField(null=False)
    altura=models.IntegerField(null=False)
    imagen = models.URLField(max_length=200, null=True, blank=True)
    
    entrenador = models.ForeignKey(
        'Entrenador',               
        on_delete=models.CASCADE, 
        null=True,                
        blank=True
    )
    def __str__(self):
      return self.nombre
  
class Entrenador(models.Model):
   
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100) 
    edad = models.IntegerField() 
    nivel = models.IntegerField(default=1) 
    fecha_de_nacimiento = models.DateField(null=True, blank=True) 
    def __str__(self):
        return f"{self.nombre} {self.apellido} (Nivel {self.nivel})"
                                