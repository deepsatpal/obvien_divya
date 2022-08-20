from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, get_user
from django.contrib import messages
from django.shortcuts import render, redirect
from contacts_import.models import Contact
from accounts.forms import AuthenticationForm, SignUpForm
from altworkz.settings import GOOGLE_RECAPTCHA_SITE_KEY, GOOGLE_RECAPTCHA_SECRET_KEY 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import send_mail
from . models import AccountActivation
import requests
import random
import string

def login_view(request):

    form = AuthenticationForm()

    if request.method == 'POST':
    
        username = request.POST.get('username')
        password = request.POST.get('password')    
    
        user = User(username=username)
            
        #print("user ", user)
        #print("User.is_active ", user.is_active)
        #print("User.is_staff ", user.is_staff)
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Either you are providing invalid username or password OR your access to this system is approved by admin. In case you belive that you are supplying correct credentials, please contact rak@bridges.com for activation of your account.')
            return render(request, 'login.html', {'form': form})    
        print("Authenticate user ", user)
        #confirm_login_allowed(user)
            
    return render(request, 'login.html', {'form': form})                

# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             print('*****************************')
#             # first_name = form.cleaned_data.get('first_name')
#             # last_name = form.cleaned_data.get('last_name')
#             # job_title = form.cleaned_data.get('job_title')
#             # organization = form.cleaned_data.get('organization')
#             # current_user = request.user
#             #
#             # createContactProfile(first_name, last_name, job_title, organization)
#
#             form.save()
#             # print(auth_user.id)
#
#
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

# def createContactProfile(first_name, last_name, job_title, organization):
#     contact, created = Contact.objects.update_or_create(
#         defaults={'user_id': 1, 'first_name': first_name, 'middle_name': '',
#                   'last_name': last_name},
#         first_name=first_name,
#         last_name=last_name,
#     )

#@csrf_exempt
def signup_view(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        ''' reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        recaptcha_verify_result = r.json()
        
        print("form valid ", form.is_valid())
                
        if form.is_valid():
        
            print("Recaptcha ", recaptcha_verify_result['success'])
        
            if recaptcha_verify_result['success']:
        
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.profile.first_name = form.cleaned_data.get('first_name')
                user.profile.last_name = form.cleaned_data.get('last_name')
                user.profile.job_title = form.cleaned_data.get('job_title')
                user.profile.organization = form.cleaned_data.get('organization')
                user.is_active = False
                user.save()
                
                user_account_activation = AccountActivation()               
                user_account_activation.activation_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))
                user_account_activation.user_id = user.id
                user_account_activation.save()
                
                print("Activation User ID ", user_account_activation.user_id)
                print("Activation String ", user_account_activation.activation_string)
               
                raw_password = form.cleaned_data.get('password1')
                #user_auth = authenticate(username=user.username, password=raw_password)
                
                send_activation_email_to_admin(user, user_account_activation.activation_string)
                
                
                return redirect('index')
                
            else:
            
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                                
            # login(request, user)

    form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form, 'recaptcha_site_key':GOOGLE_RECAPTCHA_SITE_KEY})

def send_test_email (request):
    
    
    
    #send_activation_email_to_admin('Test User', '2', '3sep-user')
    
    return HttpResponse('Please check email')

def send_activation_email_to_admin (user, activation_string):

    # .profile.first_name, user.profile.last_name, user.profile.username

    send_mail(
        f'Action Required For Activation of new Altworkz User: {user.profile.first_name} {user.profile.last_name} ({user.username})',
        '',
        'altworkzmailmgr@rakbridges.com',
        ['nadirishaq@gmail.com'],
        html_message=f'<p>A user just got registered. Please click <a href="https://www.altworkz.com/accounts/account-activation/{activation_string}">here</a> to activate this account.</p><p>Alternatively, you can also login into <a href="https://www.altworkz.com/admin/auth/user/{user.id}/change/">admin panel</a> and enable / disable account of any user you want by checking / unchecking Active.</p>',
    )

def activate_account (request, activation_code):

    print("activation code ", activation_code)

    
    try:
    
        user_to_be_activated = User.objects.filter(id=AccountActivation.objects.filter(activation_string=activation_code)[0].user_id).update(is_active=1)
    
        print('enable account ', user_to_be_activated)
    
        #user = User.objects.get(user_id=AccountActivation.objects.get(activation_code).user_id)
    
        send_mail(
            'Altworkz - Access Approved',
            '',
            'altworkzmailmgr@rakbridges.com',
            ['nadirishaq@gmail.com'],            
            html_message='Your access to Altworkz is approved by admin. You can visit <a href="www.altworkz.com">Altworkz</a> to proceed',
        ) 
    except e as exception:
    
        print("e ", exception)
    
        raise Http404("Invalid Page")

    return HttpResponse('Account activated. The user has also been notified by email.')

def home_redirect(arg):
    return redirect("/")
