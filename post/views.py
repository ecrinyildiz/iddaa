from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostCreateForm
# Create your views here.

def index(request, *args, **kwargs):
	return render(request, 'index.html', {})

def contact(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about(request, *args, **kwargs):
    return render(request, 'about.html', {})

def posts(request, *args, **kwargs):
	posts = Post.objects.all()
	return render(request, 'posts.html', {'posts':posts})

def post_detail(request, id,*args,**kwargs):
	post = get_object_or_404(Post, id = id)
	context = {
	'post':post
	}
	return render(request, 'post_detail.html', context)

def post_create_view(request, *args, **kwargs):
	form = PostCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.info(request, 'Post başarıyla kaydedildi.')
		form = PostCreateForm()


	context = {
	'form': form
	}
	return render(request, "post_create.html", context)

