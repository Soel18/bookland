from django.urls import path, include
from django.contrib.auth import views as aut_views
from app import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login_register', views.register_view, name='register'),
    path('index', views.index, name='index'),
    path('libro/<str:olid>/', views.detalle_libro, name='detalle_libro'),
    path('logout_view/', aut_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('login/google/', aut_views.LoginView.as_view(), name='google-login'),

]
