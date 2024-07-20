from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from .forms import LoginForm, RegistrationForm, ApartmentForm, MessageForm, PhotoForm
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.db.models import Prefetch, Q
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.conf import settings
    #claude version
from datetime import datetime
from django.contrib.auth import authenticate, login
import json
def my_home_view(request):
    apartments = Apartment.objects.prefetch_related(
        Prefetch('photo_set', queryset=Photo.objects.order_by('id'))
    )
    user = request.user
    return render(request, 'offcampus/home.html', {'apartments': apartments, 'user': user})
    


def logout_view(request):
    logout(request)
    return redirect('home')

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
    washer_dryer = convertToBinary(request.GET.get('washer_dryer'))
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
        apartments = [apartments.filter(rent__lte=max_price)]

    if dishwasher is not None:
        apartments = apartments.filter(dishwasher=dishwasher)
        
    if washer_dryer is not None:
        apartments = apartments.filter (washer_dryer=washer_dryer)

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
    if request.user.is_authenticated:
        # If the user is already authenticated, redirect to the desired page
        return redirect('home')

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

    # If the user is not authenticated and the request method is GET, render the login template
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


@login_required(login_url='/login/')
def message_view(request):
    apartments = Apartment.objects.all()
    apartment_data = []
    for apartment in apartments:
        owner = apartment.owner
        user = User.objects.get(id = owner.id)
        apartment_data.append({
            'name': apartment.address,
            'owner_email': user.email
        })
    # apartment_names = [apartment.address for apartment in apartments]
    return render(request, 'offcampus/messages.html', {'apartment_data': apartment_data})


"""Messaging app should have the landlordsbe associated with a specific adresses or apartment so that when 
they create a message the message goes directly to a landlord - this is for learning about the house"""

"""For subletting, users post that they are looking to sublet on the page and people can message directly from there.
Brings them to the messaging page for that sublet"""

"""Messaging can be filtered between learning about house(messages are with landlord)
Or with subletters"""

"""Need a distinction in the messaging page for subletters or learning about house. Maybe S or something on the side"""

@login_required(login_url='/login/')
def create_apartment_view(request):
    if request.method == 'POST':
        apartment_form = ApartmentForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if apartment_form.is_valid() and photo_form.is_valid():
            apartment = apartment_form.save(commit=False)
            apartment.owner = request.user
            apartment.save()
            
            photos = request.FILES.getlist('photos')
            for photo in photos:
                Photo.objects.create(apartment_id=apartment, photo=photo)
            
            return redirect('apartment_detail', pk=apartment.pk)
    else:
        apartment_form = ApartmentForm()
        photo_form = PhotoForm()
    return render(request, 'offcampus/create_apartment.html', {'apartment_form': apartment_form, 'photo_form': photo_form})


def apartment_detail_view(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    photos = Photo.objects.filter(apartment_id=apartment)
    return render(request, 'offcampus/apartment_detail.html', {'apartment': apartment, 'photos': photos})




@login_required(login_url='/login/')
def user_listings_view(request):
    # Get the logged-in user
    user = request.user
    print(user)
    # Filter apartments based on the user's ownership
    user_listings = Apartment.objects.filter(owner=user).prefetch_related(
        Prefetch('photo_set', queryset=Photo.objects.filter(apartment_id__owner=user).order_by('id'))
    )
    
    return render(request, 'offcampus/user_listings.html', {'apartments': user_listings})

@login_required(login_url='/login/')
def edit_apartment(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    photo= get_object_or_404(Photo, apartment_id = apartment_id)
    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES, instance=apartment)
        if form.is_valid():
            # Save the form data to create a new Apartment instance
            apartment = form.save(commit=False)
            apartment.owner = request.user  # Assuming you're using authentication and the user is logged in
            apartment.save()
            # Redirect to a page where you want to show the details of the newly created apartment
            # print(apartment.pk)
            if 'photo' in request.FILES and request.FILES['photo']:
                print("\n \n \n", os.listdir(), '\n \n \n')
                os.remove(settings.MEDIA_ROOT+"/"+str(apartment_id)+"/"+photo.photo_name)
                print(apartment_id)
                Photo.objects.get(apartment_id=apartment).delete()
                photo = Photo(apartment_id=apartment, photo=request.FILES['photo'])
                photo.save()
            else:
                pass
            return redirect('apartment_detail', pk=apartment.pk)  # Redirect to a view to show apartment details
    else:
        form = ApartmentForm(instance=apartment)
    return render(request, 'offcampus/edit_apartment.html', {'form': form, 'photo':photo})

from django.contrib import messages

@login_required(login_url='/login/')
def delete_apartment(request, apartment_id):
    # Retrieve the apartment object based on the primary key (apartment_id)
    apartment = get_object_or_404(Apartment, id=apartment_id)

    # Check if the logged-in user is the owner of the apartment
    if request.user == apartment.owner:
        # If the request method is POST, it means the user has confirmed the deletion
        if request.method == 'POST':
            # Delete the apartment
            apartment.delete()
            messages.success(request, 'Apartment deleted successfully.')
            return redirect('user_listings')  # Redirect to the user's listings page or any other appropriate page
        else:
            # If the request method is not POST, render the confirmation template
            return render(request, 'offcampus/confirm_delete_apartment.html', {'apartment': apartment})
    else:
        # If the logged-in user is not the owner of the apartment, show an error message
        messages.error(request, 'You are not authorized to delete this apartment.')
        return redirect('user_listings')  # Redirect to the user's listings page or any other appropriate page

@login_required(login_url='/login/')
def inbox(request):
    #messages = Message.objects.filter(recipient=request.user)
    distinct_senders = list(Message.objects.filter(recipient=request.user).values_list('sender__username', flat=True).distinct())
    users = User.objects.exclude(id=request.user.id)
    apartments = Apartment.objects.exclude(owner=request.user)
    return render(request, 'messaging/inbox.html', {'users': users, 'distinct_senders_json': json.dumps(distinct_senders), 'apartments': apartments})

@login_required
def get_latest_message(request, sender_username):
    try:
        sender = User.objects.get(username=sender_username)
        message = Message.objects.filter(recipient=request.user, sender=sender).order_by('-time_sent').first()
        if message:
            return JsonResponse({
                'message': message.content,
                'message_id': message.id,
                'is_read': message.is_read
            })
    except User.DoesNotExist:
        pass
    return JsonResponse({'message': None})

@login_required
def mark_messages_as_read(request, recipient_username):
    recipient = User.objects.get(username=recipient_username)
    unread_messages = Message.objects.filter(recipient=request.user, sender=recipient, is_read=False)
    unread_messages.update(is_read=True)
    return HttpResponse()

@login_required(login_url='/login/')
def read_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, recipient=request.user)
    message.is_read = True
    message.save()
    return render(request, 'messaging/read_message.html', {'message': message})

@login_required(login_url='/login/')
def send_message(request, username):
    recipient = get_object_or_404(User, username=username)
    
    previous_messages = Message.objects.filter(
        Q(sender=request.user, recipient=recipient) |
        Q(sender=recipient, recipient=request.user)
    ).order_by('time_sent')
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form, 'recipient': recipient, 'previous_messages': previous_messages})
