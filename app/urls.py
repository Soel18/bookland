from django.urls import path, include
from django.contrib.auth import views as aut_views
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login_register', views.register_view, name='register'),
    path('index', views.index, name='index'),
    path('libro/<str:olid>/', views.detalle_libro, name='detalle_libro'),
    path('logout/', views.logout_view, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('login/google/', aut_views.LoginView.as_view(), name='google-login'),
    path('foto/', views.foto_view, name='foto'),
    path('user_profile/', views.user_profile, name='user_profile'),    
    path('geners/', views.geners, name='geners'),
    path('writers/', views.writers, name='writers' )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)