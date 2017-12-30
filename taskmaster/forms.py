from django import forms
from django.forms import ModelForm
from .models import *

#Thsi form is to create task
class CreateTaskMaster(forms.ModelForm):
	class Meta():
		model  = TaskMaster
		fields = ["sid","tasktype","task_title","task_description","datacenter","priority","sourceincident","processingteam","duedate"]
		widgets = {
                   'sid': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   'task_title':forms.Textarea(attrs={'class': 'materialize-textarea'}),
				   'task_description':forms.Textarea(attrs={'class': 'materialize-textarea'}),
				   'sourceincident': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   'duedate' : forms.TextInput(attrs={'class': 'datepicker'}),
        		   }

#This form is to update the Task
class UpateTaskMaster(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UpateTaskMaster, self).__init__(*args, **kwargs)
		users = User.objects.all()
		self.fields['processor'].choices = [(user.pk, user.get_full_name()) for user in users]
	class Meta():
		model  = TaskMaster
		fields = ["sid","tasktype","task_title","task_description","datacenter","status","priority","sourceincident","duedate","pid","errorincident",'processor']
		widgets = {
                   'sid': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   'task_title':forms.Textarea(attrs={'class': 'materialize-textarea'}),
				   'task_description':forms.Textarea(attrs={'class': 'materialize-textarea'}),
				   'sourceincident': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   'pid': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   'errorincident': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   'duedate' : forms.TextInput(attrs={'class': 'datepicker'}),
        		   }

#This form will show the form with value
class ShowTaskMaster(forms.ModelForm):
	def __init__(self,groupid, *args, **kwargs):
		super(ShowTaskMaster, self).__init__(*args, **kwargs)
		users = User.objects.filter(groups__name=groupid)
		self.fields['processor'].choices = [(user.pk, user.get_full_name()) for user in users]
	class Meta():
		model  = TaskMaster
		fields = ["sid","tasktype","task_title","task_description","datacenter","status","priority","sourceincident","duedate","pid","errorincident",'processor']
		widgets = {
                   'sid': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   'task_title':forms.Textarea(attrs={'class': 'materialize-textarea'}),
				   'task_description':forms.Textarea(attrs={'class': 'materialize-textarea'}),
				   'sourceincident': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   'pid': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   'errorincident': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   'duedate' : forms.TextInput(attrs={'class': 'datepicker'}),
        		   }

#This form is for the comment to be added
class update_commnd(forms.ModelForm):

	class Meta():
		model  = TaskComm
		fields = ["comments"]
		widgets = {
                   'comments': forms.TextInput(attrs={'placeholder':'Please make sure its crisp and clear'})
        		   }

# This form is to update the notes
class NOTEFORM(forms.ModelForm):
	class Meta():
		model = Notes
		fields = ["note_name"]
		widgets = {
                   'note_name': forms.Textarea(attrs={'class': 'editable medium-editor-textarea comments_box'}),
				  }
