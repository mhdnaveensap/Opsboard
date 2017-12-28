from django import forms
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *
from django.forms import ModelForm

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (

			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		)

	def save(self, commit=True):
		user = super(UserRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.lastname = self.cleaned_data['last_name']
		user.firstname = self.cleaned_data['first_name']
		user.is_superuser = True
		user.is_staff = True

		if commit:
			user.save()

			return user


class EditUserProfile(UserChangeForm):

	class Meta:
		model = User
		fields = (
			'email',
			'first_name',
			'last_name',
			'password'

		)


class UpdateUserProfile(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('position','dateofbirth','team_name')
		widgets = {
                   'position': forms.Select(attrs={'class':"form-control"}),
				   'team_name': forms.Select(attrs={'class':"form-control"}),
				   'dateofbirth': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
				   # 'profile_pic' : forms.FileInput(attrs={'class': 'form-control-file'}),
        		   }


	# position = forms.CharField(required = True,label = 'position',max_length = 32)
	# teamname = forms.CharField(required = True,label = 'teamname',max_length = 32,)
	# phone = forms.IntegerField(required = True,label = 'phone',)
	# birthday=forms.DateField(required=True,label='Birthday',)
