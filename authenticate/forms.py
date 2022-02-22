from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

	class Meta:
		model = Account
		fields = ('email', 'username', 'password1', 'password2', )

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)




class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")








# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
# from django import forms



# class EditProfileForm(UserChangeForm):
# 	password = forms.CharField( widget=forms.TextInput(attrs={'type': 'hidden' }))


# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password')








# class SignUpForm(UserCreationForm):
# 	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', }) )
# 	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control' }))
# 	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control' }))
# 	#company = forms.CharField(max_length=100)

# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


# 	def __init__(self, *args, **kwargs):
# 	    super(SignUpForm, self).__init__(*args, **kwargs)

# 	    self.fields['first_name'].widget.attrs['class'] = 'form-control'
# 	    self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
# 	    self.fields['first_name'].label = ''

# 	    self.fields['last_name'].widget.attrs['class'] = 'form-control'
# 	    self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
# 	    self.fields['last_name'].label = ''

# 	    self.fields['email'].widget.attrs['class'] = 'form-control'
# 	    self.fields['email'].widget.attrs['placeholder'] = 'Email'
# 	    self.fields['email'].label = ''


# 	    self.fields['username'].widget.attrs['class'] = 'form-control'
# 	    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
# 	    self.fields['username'].label = ''
# 	    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

# 	    self.fields['password1'].widget.attrs['class'] = 'form-control'
# 	    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
# 	    self.fields['password1'].label = ''
# 	    self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

# 	    self.fields['password2'].widget.attrs['class'] = 'form-control'
# 	    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
# 	    self.fields['password2'].label = ''
# 	    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'