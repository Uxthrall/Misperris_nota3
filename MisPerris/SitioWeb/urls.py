from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.pag_index, name='pag_index'),
	url(r'^contactanos', views.pag_contactanos, name='pag_contactanos'),
	url(r'^contactanos', views.pag_list, name='pag_contactanos'),
	url(r'^ListaContact', views.list_contact, name='pag_listadoCont'),
	url(r'^rescatados', views.pag_rescatados, name='pag_rescatados'),
	url(r'^formulario', views.pag_formulario, name='pag_formulario'),
	url(r'^listar', views.pag_list, name='pag_listar'),

	url('accounts/',include('allauth.urls')),
	
]