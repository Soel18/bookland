from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libro/<str:olid>/', views.detalle_libro, name='detalle_libro'),
]
