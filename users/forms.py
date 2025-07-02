from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate
from .models import Profile

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['first_name','email','password1','password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username=self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.set_password(self.cleaned_data['password1'])
            user.save()
        return user

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Email' , max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Invalid email or password.")
            
            user = authenticate(username=user.username, password=password)
            print("Authenticated user:", user)

            if user is None:
                raise forms.ValidationError("Invalid email or password.")
            
            self.user = user
            return cleaned_data
        else:
            raise forms.ValidationError("Both email and password are required.")

    def get_user(self):
        return self.user

HEIGHT_CHOICES = [(str(i), f"{i} cm") for i in range(140, 201)]
WEIGHT_CHOICES = [(str(i), f"{i} kg") for i in range(40, 121)]
    
class ProfileForm(forms.ModelForm):
    height = forms.ChoiceField(choices=HEIGHT_CHOICES, widget=forms.Select(attrs={'class': 'input'}))
    weight = forms.ChoiceField(choices=WEIGHT_CHOICES, widget=forms.Select(attrs={'class': 'input'}))

    class Meta:
        model = Profile
        fields = ['image', 'date_of_birth', 'height', 'weight', 'skin_type']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'infos'}),
             'skin_type' :forms.Select(attrs={'class': 'input'}),
        }
