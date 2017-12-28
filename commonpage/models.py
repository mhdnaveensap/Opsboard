from django.db import models
from django.contrib.auth.models import User,Group
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
# from taskmaster.models import TeamTable
import datetime

# Create your models here.
class PositionTable(models.Model):
    position = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.position

class Team_Table(models.Model):
    Team_id = models.IntegerField(primary_key=True)
    Team_Name = models.CharField(max_length=50,default='')

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    position = models.ForeignKey(PositionTable,default='',on_delete=models.CASCADE)
    team_name = models.ForeignKey(Group,default='',null=True,on_delete=models.CASCADE)
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    useractive = models.BooleanField(default=False)
    # is_dummy = models.BooleanField(default=False)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list
    dateofbirth = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.user.username
# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)
