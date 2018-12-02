from django import forms
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "Nome completo"
            }
        )
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'input',
            "placeholder": "Email"
        }
    )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'textarea',
                "placeholder": "Sua mensagem"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email precisa ser gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'Usuario'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input',
            'placeholder': 'Senha'
        }
    ))


class RegisterForm(forms.Form):
    success_url = reverse_lazy('login')
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'Usuario'
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'Email'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input',
            'placeholder': 'Senha'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input',
            'placeholder': 'Confirme sua senha'
        }
    ))

    # validação do username na tela de cadastro
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError(f"O login {username} já esta em uso!")
        return username
    # validação do email na tela de cadastro

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(f"O email {email} já esta em uso!")
        return email
    # validação das senhas coincidirem

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("As senhas devem ser iguais!")
        return data
