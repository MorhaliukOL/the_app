from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json

from .models import Post, Comment
from .forms import PostForm, CommentForm


def blog_view(request):
    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})


@login_required
def write_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            post = Post(
                title=title,
                body=body,
                author=request.user
            )
            post.save()
            return redirect('view-post', pk=post.pk)
        else:
            return HttpResponse("Invalid data !!!")
    else:
        form = PostForm()
        return render(request, 'blog/write_post.html', {'form': form})


def view_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
    }
    response_data = {}
    if request.method == 'POST':
        com_body = request.POST.get('com_body')
        comment = Comment(
            author=request.user,
            body=com_body,
            post=post,
        )
        comment.save()
        response_data['Success'] = 'Comment saved!'
        return HttpResponse(json.dumps(response_data))

    else:
        form = CommentForm()
        context['com_form'] = form
        return render(request, 'blog/view_post.html', context)
