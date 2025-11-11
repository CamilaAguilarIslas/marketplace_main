from django.urls import path
from django.contrib.auth import views as auth_views
from.views import contact,detail, registrer 

from .forms import LoginForm

urlpatterns=[
    path('contact/', contact, name='contact' ),
    path('registrer/', registrer, name='registrer'), 
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), authetication_form=LoginForm), 
    path('detail/<int:pk>/', detail, name='detail'),
]