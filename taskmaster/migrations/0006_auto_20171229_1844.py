# Generated by Django 2.0 on 2017-12-29 13:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0005_notes_note_updateddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomm',
            name='updateddate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]