from django.shortcuts import render, redirect, get_object_or_404
from .models import PostModel
from .forms import PostCreateForm, PostUpdateForm
from django.db.models import Q


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


def post_view(request):
    request.title = 'Xayriya'
    posts = PostModel.objects.all().order_by('-id')
    search = request.GET.get('q', '')
    if search:
        posts = posts.filter(Q(title__icontains=search) | Q(body__icontains=search))
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


def update_post_view(request, id):
    instance = get_object_or_404(PostModel, id=id)
    form = PostUpdateForm(data=request.POST or None, files=request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'post-update.html', context={
        "form": form
    })
