##########################################################
#Import Statements
##########################################################
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from commonpage.models import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,HttpResponse
from django.template import Context, loader
from django import forms
from .forms import (
    UserRegistrationForm,
    EditUserProfile,
    UpdateUserProfile,
    CreateTaskMaster,
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
