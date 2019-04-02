from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostCreateForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django import forms

# Create your views here.

def index(request, *args, **kwargs):
	return render(request, 'index.html', {})

def contact(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about(request, *args, **kwargs):
    return render(request, 'about.html', {})

def posts(request, *args, **kwargs):
	posts = Post.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 5)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'posts.html', {'posts':posts})

def post_detail(request, id,*args,**kwargs):
	post = get_object_or_404(Post, id = id)
	context = {
	'post':post
	}
	return render(request, 'post_detail.html', context)



def post_delete(request, id, *args, **kwargs):
	post = get_object_or_404(Post, id = id)
	post.delete()
	context = {
	'post':post
	}
	messages.success(request,"Post silindi.")
	return redirect("/posts")

def post_update(request, id, *args, **kwargs):
	post = get_object_or_404(Post, id = id)

	if request.method == "POST":
		form = PostCreateForm(request.POST, instance=post)

		try:
			if form.is_valid():
				form.save()
				messages.success(request, 'Edit kaydedildi.')
				return redirect("/posts")
		except Exception as e:
			messages.warning(request, "Edit kaydedilmedi: {}".format(e))
	else:
		form = PostCreateForm(instance=post)

	context = {
	'post':post,
	'form':form
	}
	return render(request, "/posts", context)

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