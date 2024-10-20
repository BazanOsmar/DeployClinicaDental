from django.urls import path
from . import views
urlpatterns = [
    path('', views.renderIndex, name='Index')
]
