from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Apartment
from .forms import LoginForm, RegistrationForm
from django.template.loader import render_to_string
from django.http import JsonResponse

from django.contrib.auth import authenticate, login
def my_home_view(request):
    apartments = Apartment.objects.all()
    print("test")
    return render(request, 'offcampus/home.html', {'apartments': apartments})  # Replace with your actual template

"""def filtered_apartments(request):
    print("test")
    sublet = request.GET.get('sublet')
    if sublet == 'true':
        sublet = 1
    if sublet == 'false':
        sublet = 0
    price_range = request.GET.get('price_range')

    # Apply filters to the apartment queryset
    apartments = Apartment.objects.all()
    if sublet!=None:
        print("sublet: True")
        print(sublet)
        print(apartments)
        apartments = apartments.filter(sublet__icontains=sublet)
        print(apartments)
    if price_range:
        print("price_range: True")
        min_price, max_price = price_range.split('-')
        apartments = apartments.filter(rent__gte=min_price, rent__lte=max_price)

    return render(request, 'offcampus/home.html', {'apartments': apartments})"""
    
    #claude version
from django.http import JsonResponse
from django.template.loader import render_to_string
from datetime import datetime

def filtered_apartments(request):
    def convertToBinary(data):
        if data == 'true':
            return 1
        elif data == 'false':
            return 0
        else:
            return None
    sublet = convertToBinary(request.GET.get('sublet'))
    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')
    dishwasher = convertToBinary(request.GET.get('dishwasher'))
    move_date_start = request.GET.get('move_date_start')
    move_date_end = request.GET.get('move_date_end')
    pets_allowed = convertToBinary(request.GET.get('pets_allowed'))
    num_beds = request.GET.get('num_beds')
    num_baths = request.GET.get('num_baths')

    apartments = Apartment.objects.all()

    if sublet is not None:
        apartments = apartments.filter(sublet=sublet)

    if min_price:
        apartments = apartments.filter(rent__gte=min_price)
        
    if max_price:
        apartments = a[apartments.filter(rent__lte=max_price)]

    if dishwasher is not None:
        apartments = apartments.filter(dishwasher=dishwasher)

    if move_date_start and move_date_end:
        start_date = datetime.strptime(move_date_start, '%Y-%m-%d').date()
        end_date = datetime.strptime(move_date_end, '%Y-%m-%d').date()
        apartments = apartments.filter(move_in_date__range=(start_date, end_date))

    if pets_allowed is not None:
        apartments = apartments.filter(pets_allowed=pets_allowed)

    if num_beds:
        apartments = apartments.filter(num_beds=num_beds)

    if num_baths:
        apartments = apartments.filter(num_baths=num_baths)

    # Render the HTML for the filtered apartments list
    apartments_html = render_to_string('offcampus/apartment_list.html', {'apartments': apartments})

    return JsonResponse({'apartments_html': apartments_html})

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
    apartments = Apartment.objects.all()
    apartment_names = [apartment.address for apartment in apartments]
    return render(request, 'offcampus/messages.html', {'apartment_names': apartment_names})


"""Messaging app should have the landlordsbe associated with a specific adresses or apartment so that when 
they create a message the message goes directly to a landlord - this is for learning about the house"""


"""For subletting, users post that they are looking to sublet on the page and people can message directly from there.
Brings them to the messaging page for that sublet"""

"""Messaging can be filtered between learning about house(messages are with landlord)
Or with subletters"""

"""Need a distinction in the messaging page for subletters or learning about house. Maybe S or something on the side"""




    
