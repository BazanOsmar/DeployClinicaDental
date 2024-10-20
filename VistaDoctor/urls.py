from django.urls import path
from . import views
app_name = 'VistaDoctor'
urlpatterns = [
    path('lista-citas/', views.vistaListaCitas, name='ListaCitas')
]