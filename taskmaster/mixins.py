from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from taskmaster.models import *
from commonpage.models import UserProfile
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
import datetime


class AjaxFormMixin(object):
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():

            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            taskid = form.save(commit=False)
            my_team = self.request.user.groups.values_list('id', flat=True).first()#getting the group id for the user
            get_my_admin = UserProfile.objects.get(team_name=my_team,user__is_active=False)
            print(get_my_admin.user.id)
            taskid.processor = User.objects.get(id=get_my_admin.user.id)
            taskid.save()
            task_id = taskid.pk
            cmd_task = TaskComm()
            cmd_task.taskid = TaskMaster.objects.get(id = task_id)
            cmd_task.updatedby = self.request.user
            cmd_task.comments = "Please proceed as per the instruction in task description"
            cmd_task.save()
            print(self.request.user)
            data = {
                'message': "Task Successfully Created"
            }
            return JsonResponse(data)
        else:
            return response
