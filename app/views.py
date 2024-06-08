# app/views.py
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import RegistrationForm
import requests

#log in
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            return render(request, 'login.html')
    return render(request, 'login.html')

#Signin up
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)           
        if form.is_valid():
            user = form.save()
            login(request, user)            
            send_welcome_email(user.email, user.username)
            return redirect('foto')
        else:
            return render(request, 'register.html', {'form': form})         
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

#Logout
@login_required(login_url='login')
def logout_view(request):
    #if request.user.is_authenticated:
    #    request.user.last_activity = timezone.now() - timedelta(minutes=0.10)
    #    request.user.save()
    logout(request)
    return redirect('login')

#Send mail
def send_welcome_email(email, username):
    subject = f'¡Hola {username}!Bienvenido a Bookland!'
    message = 'Gracias por registrarte en Bookland. Esperamos que disfrutes de nuestra plataforma.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

#Home
def index(request):
    query = request.GET.get('q', '')
    libros = []
    if query:
        response = requests.get('https://openlibrary.org/search.json', params={'title': query})
        response.raise_for_status()
        data = response.json()
        libros = data.get('docs', [])
        for libro in libros:
            cover_id = libro.get('cover_i')
            if cover_id:
                libro['cover_url'] = f'https://covers.openlibrary.org/b/id/{cover_id}-L.jpg'
            else:
                libro['cover_url'] = 'https://via.placeholder.com/128x193?text=No+Cover'
    return render(request, 'index.html', {'libros': libros})

# Vista para detalles de un libro
def detalle_libro(request, olid):
    response = requests.get(f'https://openlibrary.org/works/{olid}.json')
    response.raise_for_status()
    libro = response.json()

    libro['cover_url'] = f'https://covers.openlibrary.org/b/id/{libro.get("covers")[0]}-L.jpg' if libro.get("covers") else 'https://via.placeholder.com/128x193?text=No+Cover'

    # Obtiene ediciones del libro
    ediciones_response = requests.get(f'https://openlibrary.org/works/{olid}/editions.json')
    ediciones_response.raise_for_status()  # Asegura que la solicitud fue exitosa
    ediciones = ediciones_response.json().get('entries', [])

    # Filtra las ediciones que tienen opciones de lectura
    ediciones_lectura = []
    for edicion in ediciones:
        availability = edicion.get('availability', {})
        read_url = availability.get('read', None)
        if read_url:
            ediciones_lectura.append({
                'title': edicion.get('title', 'Título no disponible'),
                'url': read_url,
                'cover_url': f'https://covers.openlibrary.org/b/id/{edicion.get("covers")[0]}-M.jpg' if edicion.get("covers") else 'https://via.placeholder.com/128x193?text=No+Cover'
            })

    return render(request, 'detalle_libro.html', {'libro': libro, 'ediciones_lectura': ediciones_lectura})
