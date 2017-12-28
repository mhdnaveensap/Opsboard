from django.contrib import admin
from taskmaster.models import StatusTable,PriorityTable,TaskTypeTable,DatacenterTable,TaskMaster


class dis_TaskMaster(admin.ModelAdmin):
    list_display=["sid","tasktype","task_title","istaskactive","datacenter","status","priority","sourceincident","processingteam","duedate"]
    ordering = ["createddate"]
    list_filter = ('tasktype','processingteam','istaskactive','duedate','status')


# Register your models here.
admin.site.register(StatusTable)
admin.site.register(PriorityTable)
# admin.site.register(TeamTable)
admin.site.register(TaskTypeTable)
admin.site.register(DatacenterTable)
admin.site.register(TaskMaster,dis_TaskMaster)
