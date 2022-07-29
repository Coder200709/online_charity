from django.shortcuts import render, redirect
from .models import PostModel


def home_view(request):
    request.title = 'Home page'
    posts = PostModel.objects.all()
    return render(request, 'index.html', context={
        'posts': posts
    })


def post_detail_view(request, id):
    post = PostModel.objects.get(id=id)
    return render(request, 'post-detail.html', context={
        'post': post
    })


def post_delete_view(request, id):
    PostModel.objects.get(id=id).delete()
    return redirect('index')
