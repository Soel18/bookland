# app/views.py
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.conf import settings
from app.forms import RegistrationForm, UserProfileForm
import requests
from django.contrib.auth import get_backends
import random

# Register view
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            backend = get_backends()[0]
            user.backend = f'{backend.__module__}.{backend.__class__.__name__}'
            login(request, user)
            send_welcome_email(user.email, user.username)
            return redirect('foto')
        else:
            return render(request, 'login_register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'login_register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            backend = get_backends()[0]
            user.backend = f'{backend.__module__}.{backend.__class__.__name__}'
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            return render(request, 'login_register.html')
    return render(request, 'login_register.html')

#Logout
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

#Send mail
def send_welcome_email(email, username):
    subject = f'¡Hola {username}!Bienvenido a Bookland!'
    message = 'Gracias por registrarte en Bookland. Esperamos que disfrutes de nuestra plataforma.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


@login_required(login_url='login')
def foto_view(request):
    user = request.user
    
    generos_populares = ['Ficción', 'No ficción', 'Misterio', 'Ciencia ficción', 'Romance', 'Fantasía', 'Aventura']

    # Guardar los géneros favoritos si el formulario se ha enviado
    if request.method == 'POST':
        favorite_genres = request.POST.getlist('favorite_genres')[:3]  # Obtener hasta tres géneros seleccionados
        user.favorite_genres = ','.join(favorite_genres)  # Guardar como una cadena separada por comas
        user.save()
        print("se pudo")

    context = {
        'username': user.username,
        'generos_populares': generos_populares,
    } 
    return render(request, 'user.html', context)

#Acualizar usuario
@login_required(login_url='login')
def user_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            print('Perfil actualizado correctamente.')
            return redirect('foto')
        else:
            print('Error al actualizar el perfil. Por favor, corrija los errores.')
    else:
        form = UserProfileForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'user.html', context)

@login_required(login_url='login')
def index(request):
    user = request.user
    favorite_genres = user.favorite_genres.split(',') if user.favorite_genres else []
    query = request.GET.get('q', '')    
    libros = []

    if favorite_genres:
        genre_queries = ' OR '.join(f'title:"{genre}"' for genre in favorite_genres)
        response = requests.get('https://openlibrary.org/search.json', params={'q': genre_queries, 'limit': 12})        
        response.raise_for_status()
        data = response.json()
        libros = data.get('docs', [])
        for libro in libros:
            cover_id = libro.get('cover_i')
            if cover_id:
                libro['cover_url'] = f'https://covers.openlibrary.org/b/id/{cover_id}-L.jpg'
            else:
                libro['cover_url'] = 'https://via.placeholder.com/128x193?text=No+Cover'

    if query:
        response = requests.get('https://openlibrary.org/search.json', params={'title': query, 'limit': 12})
        response.raise_for_status()
        data = response.json()
        libros = data.get('docs', [])
        for libro in libros:
            cover_id = libro.get('cover_i')
            if cover_id:
                libro['cover_url'] = f'https://covers.openlibrary.org/b/id/{cover_id}-L.jpg'
            else:
                libro['cover_url'] = 'https://via.placeholder.com/128x193?text=No+Cover'

    # Selecciona 4 libros aleatoriamente
    libros_random = random.sample(libros, 4) if len(libros) >= 4 else libros

    context = {
        'libros': libros,
        'libros_random': libros_random,
    }

    return render(request, 'index.html', context)


@login_required(login_url='login')
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

@login_required(login_url='login')
def geners(request):
    generos_populares = ['Ficción', 'No ficción', 'Misterio', 'Ciencia ficción', 'Romance', 'Fantasía', 'Aventura']
    libros_por_genero = {}

    for genero in generos_populares:
        response = requests.get('https://openlibrary.org/search.json', params={'subject': genero, 'limit': 8})
        response.raise_for_status()
        data = response.json()
        libros = data.get('docs', [])
        for libro in libros:
            cover_id = libro.get('cover_i')
            if cover_id:
                libro['cover_url'] = f'https://covers.openlibrary.org/b/id/{cover_id}-L.jpg'
            else:
                libro['cover_url'] = 'https://via.placeholder.com/128x193?text=No+Cover'
        libros_por_genero[genero] = libros

    context = {
        'libros_por_genero': libros_por_genero,
    }

    return render(request, 'generos.html', context)

def generate_random_name():
    first_names = [
        "John", "Mary", "James", "Linda", "Michael", "Patricia", "David", "Jennifer"
    ]
    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia"
    ]
    
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def get_author_details(author_key):
    try:
        if not author_key.startswith('/authors/'):
            author_key = f'/authors/{author_key}'
        response = requests.get(f'https://openlibrary.org{author_key}.json')
        if response.status_code == 200:
            return response.json()
        return {}
    except requests.RequestException as e:
        print(f"Error fetching author details: {e}")
        return {}

@login_required(login_url='login')
def writers(request):
    query = request.GET.get('q', '')
    if not query:
        query = generate_random_name()

    authors = []
    response = requests.get('https://openlibrary.org/search/authors.json', params={'q': query, 'limit': 8})
    if response.status_code == 200:
        data = response.json()
        for author in data.get("docs", []):
            author_key = author.get("key").split("/")[-1]  # Extract the key like OL229501A
            authors.append({
                "name": author.get("name", "Nombre no disponible"),
                "key": author_key,
                "description": "Biografía no disponible",  # Description might not be available in search results
                "image_url": f'https://covers.openlibrary.org/a/olid/{author_key}-M.jpg' if author_key else 'https://via.placeholder.com/256x256?text=No+Photo'
            })
    else:
        print("Error al obtener autores:", response.status_code)

    context = {
        "authors": authors,
        'query': query
    }

    return render(request, 'escritores.html', context)
