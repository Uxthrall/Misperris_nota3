from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

def create_user_profile(request,user, **kwargs):
    profile =Profile.objects.create(user=user)
    profile.save()


# Create your models here.
class Post(models.Model):
    CorreoElectronico=models.CharField(max_length=100)
    Run=models.CharField(max_length=10)
    Nombre=models.CharField(max_length=50)
    FechaNacimiento=models.DateField()
    Telefono=models.IntegerField()
    region=models.CharField(max_length=50)
    comuna=models.CharField(max_length=50)
    tipoCasa=models.CharField(max_length=50)
    Perro=models.CharField(max_length=50,default='SOME STRING')

    def __str__ (self):
        return self.Run

class formulario(models.Model):
    nombre=models.CharField(max_length=100)
    Raza=models.CharField(max_length=50)
    Descripcion=models.CharField(max_length=200)
    image=models.ImageField(upload_to='albums', default='SOME STRING')
    estado=models.CharField(max_length=50)
    

    def __str__ (self):
        return self.nombre