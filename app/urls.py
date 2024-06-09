from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('login_register', views.register_view, name='register_view'),
    path('index', views.index, name='index'),
    path('libro/<str:olid>/', views.detalle_libro, name='detalle_libro'),
]
