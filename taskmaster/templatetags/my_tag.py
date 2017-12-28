from django import template
from taskmaster.models import *

register = template.Library()

# filter the url and give only the number
@register.filter(name='is_incident')
def is_incident(value):

    return value.split("/")[-1]

# give the count of active task for based on the task id
@register.filter(name='find_count_BNG')
def find_count_BNG(value, arg):
    typ_set = TaskMaster.objects.filter(istaskactive=True,tasktype__id=value,processingteam=arg).count()

    return typ_set
