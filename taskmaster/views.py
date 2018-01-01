##########################################################
#Import Statements
##########################################################
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,Group
from taskmaster.models import *
from commonpage.models import UserProfile
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,HttpResponse
from django.template import Context, loader
from django import forms
from django.utils import timezone
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.views.generic import FormView
from time import sleep
from taskmaster.taskcounter import *
from django.forms.models import model_to_dict
from .forms import (
    CreateTaskMaster,
    UpateTaskMaster,
    update_commnd,
    ShowTaskMaster,
    NOTEFORM,
    )
from .mixins import AjaxFormMixin
# from .models import MobileDB
import logging
import json
import csv
import os
import sys
import pytz

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

# This function to update and change the task status in MY task bashboard page
@login_required(login_url="/user/login")
def MY_TASK_CMD(request):
    try:

        data = {}
        # Getting the task id and cmd START
        taskid = request.GET['tskid']
        my_cmd = request.GET['cmd_text']
        my_status = request.GET['statusnm']
        my_que_stat = request.GET['task_que']
        # Getting the task id and cmd End

        # Getting the task id and cmd START
        task_commnd_id = TaskComm.objects.get(taskid=taskid,islastcommand=True)
        task_commnd = TaskComm.objects.get(pk=task_commnd_id.id)
        task_commnd.islastcommand = False
        task_commnd.updateddate = task_commnd.updateddate
        # Getting the task id and cmd End

        #Changing the status and putting the ticket back to queue START
        chng_status_id = TaskMaster.objects.get(id=taskid)
        if my_status == 'Complete':
            chng_status_id.istaskactive = False

        chng_status_id.status = StatusTable.objects.get(status=my_status)


        if my_que_stat == "Yes":
            my_team = request.user.groups.values_list('id', flat=True).first()#getting the group id for the user
            get_my_admin = UserProfile.objects.get(team_name=my_team,user__is_active=False)
            chng_status_id.processor = User.objects.get(id=get_my_admin.user.id)
        #Changing the status and putting the ticket back to queue END

        # Updating the new cmd START
        new_cmd = TaskComm()
        new_cmd.comments = my_cmd
        new_cmd.islastcommand = True
        new_cmd.taskid = TaskMaster.objects.get(pk=taskid)
        new_cmd.updatedby = request.user
        new_cmd.updateddate = timezone.now()
        # Updating the new cmd END

        task_commnd.save()
        chng_status_id.save()
        new_cmd.save()

        data['status'] = "Got your update and successfully saved";
        return HttpResponse(json.dumps(data),content_type="application/json")
    except Exception as e:
        data['status'] = str(e);
        return HttpResponse(json.dumps(data),content_type="application/json")


@login_required(login_url="/user/login")
def dashboard(request):
    # AREA FOR NOTE START
    my_team = request.user.groups.values_list('id', flat=True).first()#getting the group id for the user
    note_id = get_object_or_404(Notes, note_active=True,note_updatedby__user_profile__team_name=my_team)
    form_notes = NOTEFORM(instance=note_id)
    # AREA FOR NOTE END HERE

    # Queryset for my unprocessed task start
    two_days_back = date.today() - timedelta(days=2)
    task_not_update = TaskComm.objects.filter(islastcommand=True,updateddate__lte=two_days_back,taskid__istaskactive=True)
    # Queryset for my unprocessed task end

    # Queryset for my task start
    mytask = TaskComm.objects.filter(islastcommand=True,taskid__istaskactive=True,taskid__processor=request.user.id)
    # Queryset for my task end
    return render(request, 'dashboard/dash_board.html',{'form_notes': form_notes,'my_task':mytask,'old_task':task_not_update})

# This function updates the notes in the dashboard
@login_required(login_url="/user/login")
def board_update_note(request):
    try:
        data ={}
        if request.method == 'POST':
            my_team = request.user.groups.values_list('id', flat=True).first()#getting the group id for the user
            note_id = get_object_or_404(Notes, note_active=True,note_updatedby__user_profile__team_name=my_team)
            form = NOTEFORM(request.POST,instance=note_id)
            if form.is_valid():
                form_update = form.save(commit=False)
                form_update.note_updatedby = request.user
                form_update.note_updateddate = datetime.datetime.now()
                form_update.save()
                data['stat'] = "ok";
                return HttpResponse(json.dumps(data),content_type="application/json")
            else:
                data['stat'] = "error";
                return HttpResponse(json.dumps(data),content_type="application/json")
    except Exception as e:
        data['stat'] = str(e);
        return HttpResponse(json.dumps(data),content_type="application/json")

# This function shows the notes in the dashboard
@login_required(login_url="/user/login")
def board_show_note(request):
    my_team = request.user.groups.values_list('id', flat=True).first()#getting the group id for the user
    notes = Notes.objects.filter(note_active=True,note_updatedby__user_profile__team_name=my_team)
    return render(request, 'dashboard/note.html', {'notes': notes,})

# This function is for all task in active
@login_required(login_url="/user/login")
def alltask(request):
    # Queryset for all task start
    alltask = TaskComm.objects.filter(islastcommand=True,taskid__istaskactive=True)
    # Queryset for all task end
    return render(request, 'task/alltask.html',{'alltask':alltask})

# This function is for completed task in active
@login_required(login_url="/user/login")
def completedtask(request):
    # Queryset for completed task start
    completedtask = TaskComm.objects.filter(islastcommand=True,taskid__istaskactive=False)
    # Queryset for completed task end
    return render(request, 'task/completed_task.html',{'completedtask':completedtask})

# The below class create Task with a AJAX call
class ajaxtaskcreate(AjaxFormMixin,FormView):
    form_class = CreateTaskMaster
    template_name = 'task/task.html'
    success_url = '/form-success/'
# The below function gives the data to the table
@login_required(login_url="/user/login")
def taskpage(request):

    try:
        data = {}
        form = CreateTaskMaster()
        get_lab = find_count()
        TaskTypeTag = TaskTypeTable.objects.all()
        my_team = request.user.groups.values_list('id', flat=True).first()#getting the group id for the user
        final_set = TaskComm.objects.filter(islastcommand=True,taskid__istaskactive=True,taskid__processingteam=my_team)
        task_without_proc = final_set.filter(taskid__processor__is_active=False)
        return render(request, 'task/task.html', {'form': form,'all_active_task':final_set,'with_out_proc':task_without_proc, 'TaskTypeTag':TaskTypeTag,'task_count':get_lab})
    except Exception as e:
        print("Show task :" + str(e))

# The below function shows the selected taskid in the update screen
@login_required(login_url="/user/login")
def show_task(request, taskid):
    try:
        data ={}
        task_id = get_object_or_404(TaskMaster, pk=taskid)
        group_id = request.user.groups.values_list('name', flat=True).first()
        form = ShowTaskMaster(instance=task_id,groupid=group_id)#seding group to get the dropdown accordingly
        form_cmd = update_commnd()#send the form to update the commants of the task
        return render(request, 'task/updatetask.html', {'form': form,'form_cmd':form_cmd,'taskid':task_id})
    except Exception as e:
        print("show update Task Error - "+str(e))

# This function updates the task
@login_required(login_url="/user/login")
def updatetaskpage(request,taskid):
    try:
        data ={}
        if request.method == 'POST':

            task_id = get_object_or_404(TaskMaster, pk=taskid)
            form = UpateTaskMaster(request.POST,instance=task_id)
            if form.is_valid():
                form_update = form.save(commit=False)

                if form_update.status.status == "Complete":
                    form_update.istaskactive = False

                form_update.save()
                data['stat'] = "ok";
                return HttpResponse(json.dumps(data),content_type="application/json")
            else:
                data['stat'] = "error";
                return HttpResponse(json.dumps(data),content_type="application/json")


    except Exception as e:
        data['stat'] = str(e);
        return HttpResponse(json.dumps(data),content_type="application/json")

#This function shows the command for the task id and updated the comment.
@login_required(login_url="/user/login")
def command(request,taskid):
    try:
        data = {}
        command_list = TaskComm.objects.filter(taskid=taskid)
        form = update_commnd()
        if request.method == 'POST':
            form = update_commnd(request.POST)
            if form.is_valid():
                task_commnd_id = TaskComm.objects.get(taskid=taskid,islastcommand=True)
                task_commnd = TaskComm.objects.get(pk=task_commnd_id.id)
                task_commnd.islastcommand = False
                task_commnd.updateddate = task_commnd.updateddate
                task_commnd.save()
                form_update = form.save(commit=False)
                form_update.updatedby = request.user
                print(taskid)
                form_update.taskid = TaskMaster.objects.get(id = taskid)
                form_update.save()


                # task_commnd.save()
                data['stat'] = "ok";
                return HttpResponse(json.dumps(data),content_type="application/json")
            else:
                data['stat'] = "error";
                return HttpResponse(json.dumps(data),content_type="application/json")

        return render(request, 'task/commands.html', {'form': form,'commnd_list':command_list})

    except Exception as e:
        data['stat'] = str(e);
        return HttpResponse(json.dumps(data),content_type="application/json")

@login_required(login_url="/user/login")
def test_timezone(request):
    # note_id = get_object_or_404(Notes, note_active=True)
    timenow = timezone.now()
    return render(request, 'dashboard/testtime.html', {'timenow': timenow,})
