from django.urls import path
from . import views
urlpatterns = [
    path('', views.renderIndex, name='Index'),
    path('login/', views.Login, name='login'),
    path('registro/', views.SignUp, name='signup'),
    path('singout/', views.signOut, name='signout')
]
