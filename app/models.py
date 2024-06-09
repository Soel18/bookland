from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Prefer not to say'),
    ]
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)    
    biography = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=gender_choices)

    def __str__(self):
        return self.username



class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)  # Fecha de nacimiento
    country = models.CharField(max_length=100, null=True, blank=True)  # País

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    published_date = models.DateField()
    # Puedes añadir un campo para almacenar el archivo del libro (pdf, epub, etc.)
    # file = models.FileField(upload_to='books/files/')

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.book.title}'

class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    stars = models.PositiveIntegerField(default=1)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.stars} stars by {self.user.username} for {self.book.title}'
