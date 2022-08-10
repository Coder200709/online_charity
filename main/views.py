from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostCreateForm


def post_create_view(request):
    form = PostCreateForm()

    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = PostModel(
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
                image=form.cleaned_data['image']
            )
            post.save()
            return redirect('index')
    return render(request, 'post-create.html', context={
        'form': form
    })


def home_view(request):
    request.title = 'Home page'
    posts = PostModel.objects.all().order_by('-id')
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
