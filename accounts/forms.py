from django import forms


class LoginForm(forms.Form):

	username = forms.CharField(max_length=100, label="Kullanıcı adı")
	password = forms.CharField(max_length=100, label="Parola", widget=forms.PasswordInput)



class SigninForm(forms.Form):

	username = forms.CharField(max_length=100, label="Kullanıcı adı")
	password = forms.CharField(max_length=100, label="Parola", widget=forms.PasswordInput)
	password2 = forms.CharField(max_length=100, label="Parola", widget=forms.PasswordInput)
