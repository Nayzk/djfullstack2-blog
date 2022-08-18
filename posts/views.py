from django.shortcuts import render , redirect



# Create your views here.
from .models import Post
from .forms import PostForm


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html',{'mahmoud':posts})


def single_post(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'single.html',{'single_post': post})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    return render(request,'new.html',{'form': form})


def edit_post(request,id):
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
    else:
        form = PostForm(instance=post)
    return render(request,'edit.html',{'form': form})


def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/blog/')