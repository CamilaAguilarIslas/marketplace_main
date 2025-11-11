# Marketplace

#  Signup y Login en Forms.py 
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Item

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu usuario',
            'class': 'form-control'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'password',
            'class': 'form-control'
        }
    ))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Tu Usuario',
            'class': 'form-control'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Tu Email',
            'class': 'form-control'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Repite Password',
            'class': 'form-control'
        }
    ))

```
# Funciones en views.py
```python

from django.shortcuts import render
from django.contrib.auth import logout


from.models import Item, Category
from django.shortcuts import get_object_or_404, redirect


from .forms import SignupForm


# Create your views here.
def home(request):
    Items = Item.objects.filter(is_solid=False)
    Categories = Category.objects.all()
    context={
        'items': Items,
        'categories': Categories
    }
    return render(request,'store/home.html', context)


def contact(request):
    context ={
        'msg':'¿Quieres otros productos? Contactame'
    }
    return render(request,'store/contact.html',context)


def detail(request, pk):
    item=get_object_or_404(Item, pk=pk)
    related_items=Item.objects.filter(category=item.category, is_solid=False).exclude(pk=pk)[0:3]


    context={
        'item':item,
        'related_items': related_items
    }
    return render(request,'store/item.html',context)


def register(request):
    if request.metod =="POST":
        form = SignupForm(request.POST)


        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form =SignupForm()


    context ={
        'form':form
    }


    return render(request, 'store/signup.html', context)
```

# Templates templates/store login 