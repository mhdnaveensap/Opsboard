##########################################################
#Import Statements
##########################################################
import warnings

from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import  QueryDict
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.six.moves.urllib.parse import urlparse, urlunparse
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from commonpage.models import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,HttpResponse
from django.template import Context, loader
from django import forms
from .forms import (
    UserRegistrationForm,
    EditUserProfile,
    UpdateUserProfile,
    )
from django.contrib.auth.forms import (
    UserChangeForm,
    PasswordChangeForm,
    )
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from time import sleep
from django.forms.models import model_to_dict

# from .models import MobileDB
import logging
import json
import csv
import os
import sys

init_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(init_path)

##########################################################
#Global Variables
##########################################################
# Get an instance of a logger
logger = logging.getLogger(__name__)
##########################################################
#Views
##########################################################
#Q Create an API which takes a number and returns the factorial in JSON format.

# This login functon check for the username and password and also useractive state
@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            userObj = form.cleaned_data
            username = userObj['username']

            is_active_user = UserProfile.objects.get(user__username=username)

            if is_active_user.useractive == True:

                # Ensure the user-originating redirection url is safe.
                if not is_safe_url(url=redirect_to, host=request.get_host()):
                    redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

                # Okay, security check complete. Log the user in.
                auth_login(request, form.get_user())

                return HttpResponseRedirect(redirect_to)
            else:
                return render(request, 'registration/acc_not_act.html')

    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)


# def home(request):
#     return render(request, 'registration/acc_not_act.html')

def register(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password1']


            form.save()

            user = authenticate(username=username, password=password)
            auth_login(request, user)
            print("IS LOGIN")
            # jso = Javascript("alertme")
            # display_javascript(jso)

            return redirect('/user/teamdetails')

    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def update_team(request):
    try:

        if request.method == 'POST':
            form = UpdateUserProfile(request.POST)
            if form.is_valid():

                profile = form.save(commit=False)
                profile.user = User.objects.get(username=request.user)

                print(profile.team_name)
                my_group = Group.objects.get(name=profile.team_name)
                print("working1")
                my_group.user_set.add(request.user)
                print("working2")

                # if 'profile_pic' in request.FILES:
                #     profile.profile_pic = request.FILES['profile_pic']
                # else:
                #     profile.profile_pic = "profile_pics/noprofile.png"


                profile.save()

                return redirect('/user/logout')
        else:
            form = UpdateUserProfile()
        return render(request, 'registration/update_team.html', {'form': form})

    except Exception as e:
        pass

@login_required(login_url="/user/login")
def view_profile(request):

    if request.method == 'POST':
        form = EditUserProfile(request.POST, instance=request.user)
        form_chpass = PasswordChangeForm(data=request.POST, user=request.user)
        print (request.POST)
        if 'btneditinfo' in request.POST:
            status = {'status': 'Profile Note saved.Please check'}
            if form.is_valid():
                form.save()
                status = {'status': 'Profile saved'}
                return render(request, 'registration/profile.html', context=status)
            else:
                return render(request, 'registration/profile.html', context=status)
        elif 'passcng' in request.POST:
            status = {'status': 'Please check old password is correct and check is new password is identical'}
            if form_chpass.is_valid():
                form_chpass.save()
                update_session_auth_hash(request, form_chpass.user)
                return redirect('/')
            else:
                return render(request, 'registration/profile.html', context=status)
        else:
            return redirect('/profile/')

    else:
        form = EditUserProfile(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/profile.html', args)

def handler404_view(request):
    return render(request, 'registration/404.html', status=404)

def handler500_view(request):
    return render(request, 'registration/500.html', status=500)

def test_view(request):
    return render(request,'registration/testing.html')
