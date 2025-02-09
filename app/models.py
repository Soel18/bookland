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
    favorite_genres = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.username



class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)  # Fecha de nacimiento
    country = models.CharField(max_length=100, null=True, blank=True)  # País
    #reaction = models.BooleanField()

    def __str__(self):
        return self.name

class Book(models.Model):
    olid = models.CharField(max_length=50, unique=True)  # Campo para el identificador de Open Library
    title = models.CharField(max_length=200)
    description = models.TextField()

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
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Rating by {self.user.username} for {self.book.title}'
