from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    #Escribo los campos para que diga una alerta de que son obligatorios.
    first_name = forms.CharField(label='Nombre', required=True)
    last_name  = forms.CharField(label='Apellido', required=True)
    password1  = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2  = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    email      = forms.EmailField(label='Correo Electrónico', required=True)

    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2'] #Pedir solo el nombre, email y contraseñas

    #Función que verifica que el campo de nombre no este vacío.
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("El nombre es obligatorio.")
        return first_name

    #Función que verifica que el campo apellido no esté vacío.
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("El apellido es obligatorio.")
        return last_name

    #Función que verifica que el campo email no esté vacío.
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("El email es obligatorio.")
        #Verifico que no esté ya registrado el email
        if User.objects.filter(username=email).exists():
            raise ValidationError("Este email ya está registrado. Usa uno diferente.")

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coiciden.")
        return password2
    
    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])

        #El nombre de usuario será el correo.
        user.username = self.cleaned_data['email']

        if commit:
            user.save()
        return user    