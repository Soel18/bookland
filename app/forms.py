from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Comment, Rating

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'gender', 'password1', 'password2']
        widgets = {
            'gender': forms.Select(choices=CustomUser.gender_choices),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['biography', 'profile_picture']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text'] 

class RatingForm(forms.ModelForm):
    like = forms.BooleanField(required=False)
    dislike = forms.BooleanField(required=False)
    class Meta:
        model = Rating
        fields = ['like', 'dislike']

