from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User,Group
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
import datetime

# Create your models here.
class StatusTable(models.Model):
    status = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.status


class PriorityTable(models.Model):
    priority = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.priority

# class TeamTable(models.Model):
#     team = models.CharField(max_length=20,default='')
#
#     def __str__(self):
#         return self.team

class TaskTypeTable(models.Model):
    tasktype = models.CharField(max_length=30,default='')
    icon = models.CharField(max_length=50,default='fiber_new')

    def __str__(self):
        return self.tasktype

class DatacenterTable(models.Model):
    datacenter = models.CharField(max_length=10,default='')

    def __str__(self):
        return self.datacenter


class TaskMaster(models.Model):
      sid = models.CharField(max_length=3)
      # Remember to change the default value in processor in production
      processor = models.ForeignKey(User,null=True,on_delete=models.CASCADE,default=1)
      tasktype = models.ForeignKey(TaskTypeTable, null=True,on_delete=models.CASCADE)
      task_title = models.TextField(null=True)
      task_description = models.TextField(null=True)
      datacenter = models.ForeignKey(DatacenterTable,null=True,on_delete=models.CASCADE)
      priority = models.ForeignKey(PriorityTable, null=True,on_delete=models.CASCADE)
      status = models.ForeignKey(StatusTable, default=1,on_delete=models.CASCADE)
      pid = models.IntegerField(null=True)
      sourceincident = models.CharField(max_length=250,null=True)
      errorincident = models.CharField(max_length=250,null=True)
      processingteam = models.ForeignKey(Group, null=True,on_delete=models.CASCADE)
      createddate = models.DateField(("Date"), default=datetime.date.today)
      duedate = models.DateField(("Date"), default=datetime.date.today)
      istaskactive = models.BooleanField(default=True)

class TaskComm(models.Model):
    taskid  = models.ForeignKey(TaskMaster,null=True,on_delete=models.CASCADE)
    comments = models.TextField(default="")
    updateddate = models.DateTimeField(default=timezone.now)
    islastcommand = models.BooleanField(default=True)
    updatedby = models.ForeignKey(User,null=True,on_delete=models.CASCADE)

class Notes(models.Model):
    note_name = models.TextField(null=True)
    note_updatedby = models.ForeignKey(User,null=True,on_delete=models.CASCADE,default=1)
    note_updateddate = models.DateTimeField(("Date"), default=datetime.datetime.now)
    note_active = models.BooleanField(default=True) 
