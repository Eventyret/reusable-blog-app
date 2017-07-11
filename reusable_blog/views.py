# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.shortcuts import redirect
 
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})

def post_detail(request, id):
    post  = get_object_or_404(Post, pk=id)
    post.views += 1 # clock up the number of post views
    post.save()
    return render(request, "postdetail.html",{'post': post})

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/blogpostform.html', {'form': form})

def edit_post(request, id):
   post = get_object_or_404(Post, pk=id)
   if request.method == "POST":
       form = BlogPostForm(request.POST, request.FILES, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect(post_detail, post.pk)
   else:
       form = BlogPostForm(instance=post)
   return render(request, 'blog/blogpostform.html', {'form': form})