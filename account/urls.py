from django.urls import path
from . import views
urlpatterns = [
    path('', views.renderIndex),
    path('login/', views.renderLogin, name='login'),
    path('registro/', views.renderSignUp, name='signup'),
]
