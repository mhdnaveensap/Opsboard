##########################################################
#Import Statements
##########################################################
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,Group
from taskmaster.models import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,HttpResponse
from django.template import Context, loader
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from time import sleep
from taskmaster.taskcounter import *
from django.forms.models import model_to_dict
from .forms import (
    CreateTaskMaster,
    UpateTaskMaster,
    update_commnd,
    ShowTaskMaster,
    )

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


@login_required(login_url="/user/login")
def dashboard(request):
    return render(request, 'dashboard/dash_board.html')

# The below function gives the data to the table and save the data in post method
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

        if request.method == 'POST':
            form = CreateTaskMaster(request.POST)

            if form.is_valid():
                taskid = form.save()
                task_id = taskid.pk
                cmd_task = TaskComm()
                cmd_task.taskid = TaskMaster.objects.get(id = task_id)
                cmd_task.updatedby = request.user
                cmd_task.comments = "Please proceed as per the instruction in task description"
                cmd_task.save()
                data['stat'] = "ok";
                return HttpResponse(json.dumps(data),content_type="application/json")
            else:
                data['stat'] = "error";
                form = CreateTaskMaster()
                TaskTypeTag = TaskTypeTable.objects.all()
                final_set = TaskComm.objects.filter(islastcommand=True,taskid__istaskactive=True)
                return render(request, 'task/task.html', {'form': form,'all_active_task':final_set, 'TaskTypeTag':TaskTypeTag,'task_count':get_lab,'all_task':final_set.count(),'with_out_proc':task_without_proc.count()})


        return render(request, 'task/task.html', {'form': form,'all_active_task':final_set, 'TaskTypeTag':TaskTypeTag,'task_count':get_lab,'all_task':final_set.count(),'with_out_proc':task_without_proc.count()})

    except Exception as e:
        pass

# The below function shows the selected taskid in the update screen
@login_required(login_url="/user/login")
def show_task(request, taskid):
    try:
        data ={}
        task_id = get_object_or_404(TaskMaster, pk=taskid)
        group_id = request.user.groups.values_list('name', flat=True).first()
        form = ShowTaskMaster(instance=task_id,groupid=group_id)#seding group to get the dropdown accordingly
        form_cmd = update_commnd()
        return render(request, 'task/updatetask.html', {'form': form,'form_cmd':form_cmd,'taskid':task_id})
    except Exception as e:
        pass

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
        raise

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
        raise
