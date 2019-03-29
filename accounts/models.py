from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=100, label="Kullanıcı adı")
	password = models.TextField(max_length=100, label="Parola", widget=forms.PasswordInput)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post:posts', kwargs={'id': self.id})
