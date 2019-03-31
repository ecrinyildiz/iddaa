from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120, verbose_name='Başlık')
	content = models.TextField(verbose_name='İçerik')
	updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Yayımlanma Tarihi')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	def __str__(self):
		return self.title
		return self.updated

	def get_absolute_url(self):
		return reverse('post:posts', kwargs={'id': self.id})
