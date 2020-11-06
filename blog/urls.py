from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicacion_lista, name='publicacion_lista'),
<<<<<<< HEAD
    path('publicacion/<int:pk>/', views.publicacion_detalle, name='detalle_publicacion'),
    path('publicacion/nueva', views.publicacion_nueva, name= 'publicacion_nueva'),
    path('publicacion/<int:pk>/editar/', views.publicacion_editar, name='publicacion_editar'),
    path('publicacion/borrador/lista', views.publicacion_borrador_lista, name='publicacion_borrador_lista'),
    path('publicacion/<int:pk>/publicar/', views.publicacion_publicar, name='publicacion_publicar'),
=======
    path('publicacion/<int:pk>/', views.publicacion_detalle, name='publicacion_detalle'),
>>>>>>> a4624866c416a4a56c456157e9cb57115885e80b
]
