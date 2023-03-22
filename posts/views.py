from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
# Create your views here.


class PostList(generic.ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"


class PostDetail(generic.DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


class PostCreate(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content"]


class PostEdit(generic.UpdateView):
    model = Post
    template_name = "posts/post_edit.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post-list")


class PostDelete(generic.DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("post-list")