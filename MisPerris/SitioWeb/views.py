from django.shortcuts import render, redirect, render_to_response

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Post,formulario 
# Create your views here.

def pag_index(request):
	return render(request,'index.html')


def pag_contactanos(request):
	
		form= formulario.objects.all()
		autor = Post()
		if request.method=="POST":

			autor.CorreoElectronico = request.POST['correo']
			autor.Run = request.POST['run']
			autor.Nombre = request.POST['nombre']
			autor.FechaNacimiento = request.POST['fecha_nacimiento']
			autor.Telefono = request.POST['telefono']
			autor.region = request.POST['cosa']
			autor.comuna = request.POST['opt']
			autor.tipoCasa = request.POST['Vivienda']
			autor.Perro=request.POST['NomPerru']
			
			autor.save()
			estado=True

		contex={'formularios':form}
		return render(request,'Contactanos.html', contex)
		
def pag_rescatados(request):
	return render(request,'Perritos.html')		

def pag_formulario(request):
		estado = False
		forms=formulario()
		if request.method=="POST":
			if request.POST['nombree']!="" and request.POST['raza']!="" and request.FILES['docfile']!="" and request.POST['descripcion']!="":
				forms.nombre= request.POST['nombree']
				forms.Raza = request.POST['raza']
				forms.Descripcion= request.POST['descripcion']
				forms.image= request.FILES['docfile']
				forms.estado= request.POST['Estado']
				forms.save()
				estado=True

		dic={'estado': estado}
		return render(request,'formulario.html', dic)

def pag_list(request):
	form= formulario.objects.all()
	contex={'formularios':form}
	return	render(request,'listar.html',contex)



	

def list_contact(request):
	cont=Post.objects.all()
	contex={'posts':cont}
	return render (request,'listContactos.html', contex)



