# Generated by Django 2.0 on 2017-12-28 00:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatacenterTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datacenter', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PriorityTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StatusTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TaskComm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(default='')),
                ('updateddate', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date')),
                ('islastcommand', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=3)),
                ('task_title', models.TextField(null=True)),
                ('task_description', models.TextField(null=True)),
                ('pid', models.IntegerField(null=True)),
                ('sourceincident', models.CharField(max_length=250, null=True)),
                ('errorincident', models.CharField(max_length=250, null=True)),
                ('createddate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('duedate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('istaskactive', models.BooleanField(default=True)),
                ('datacenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskmaster.DatacenterTable')),
                ('priority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskmaster.PriorityTable')),
                ('processingteam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('processor', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskmaster.StatusTable')),
            ],
        ),
        migrations.CreateModel(
            name='TaskTypeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasktype', models.CharField(default='', max_length=30)),
                ('icon', models.CharField(default='fiber_new', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestTAB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sam', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='taskmaster',
            name='tasktype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskmaster.TaskTypeTable'),
        ),
        migrations.AddField(
            model_name='taskcomm',
            name='taskid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskmaster.TaskMaster'),
        ),
        migrations.AddField(
            model_name='taskcomm',
            name='updatedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]