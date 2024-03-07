from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Apartment
from .forms import LoginForm, RegistrationForm

from django.contrib.auth import authenticate, login
def my_home_view(request):
    apartments = Apartment.objects.all()
    return render(request, 'offcampus/home.html', {'apartments': apartments})  # Replace with your actual template

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the user credentials are valid
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User authentication successful
                login(request, user)
                # Redirect to home page or dashboard after login
                return redirect('home')
            else:
                # User authentication failed
                form.add_error('username', 'Invalid username or password')

    else:
        form = LoginForm()
    return render(request, 'offcampus/login.html', {'form': form})


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Check if passwords match
            if password == confirm_password:
                # Create a new user
                User.objects.create(
                    username=username,
                    email=email,
                    password=make_password(password)
                )

                # Redirect to the login page after successful registration
                return redirect('login')
            else:
                # Passwords do not match, add an error to the form
                form.add_error('confirm_password', 'Passwords do not match')

    else:
        form = RegistrationForm()
    return render(request, 'offcampus/registration.html', {'form': form})

def message_view(request):
    return render(request, 'offcampus/messages.html')


    
