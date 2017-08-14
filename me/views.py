# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Post
from .forms import PostForm
from django.views import View
from django.views.generic.list import ListView
# Create your views here.
class IndexView(View):


    def get(self,request,*args,**kwargs):
        return render(request,'me/index.html',{})


class PostCreate(View):


    def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_list', pk=post.pk)
        else:
            form = PostForm()
        return render(request,'me/edit.html', {'form': form})


    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, 'me/edit.html', {'form': form})




class PostList(ListView):
    model =Post

    def post_list(request):
        posts = Post.objects.all()
        return render(request,'me/post_list.html',{'posts':posts})

    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        return render(request,'me/post_list.html',{'posts':posts})