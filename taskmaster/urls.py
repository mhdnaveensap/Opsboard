#############################################################################
# IMPORT STATEMENTS                                                         #
#############################################################################

from django.conf.urls import url,include
from django.urls import path
from taskmaster.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)

#############################################################################
#URL Patterns                                                               #
#############################################################################
app_name = 'taskpg'

urlpatterns = [
                    url(r'^Task/$', taskpage,name="task_master"),
                    path('Task/<int:taskid>', show_task,name='show_task'),
                    path('Task/<int:taskid>/update', updatetaskpage,name='updatetask_page'),
                    path('command/<int:taskid>', command,name='command'),
                    url(r'^$', dashboard,name="dash_board"),
                    url(r'^note_show$', board_show_note,name="note_show"),
                    url(r'^note_update$', board_update_note,name="note_update"),
              ]
