from taskmaster.models import *


def find_count():
    tasktyp = TaskTypeTable.objects.all()
    task_count = {}
    for ttype in tasktyp:
        typ_set = TaskMaster.objects.filter(istaskactive=True,tasktype__id=ttype.id).count()
        task_count[ttype.id] = typ_set

    return task_count
