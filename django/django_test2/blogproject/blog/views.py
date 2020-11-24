from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from markdown import markdown

from .models import Post


def index(request):
    # return render(request,'blog/index.html',context={
    #     'title':'我的博客首页',
    #     'welcome':'欢迎访问'
    # })
    post_list=Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.body=markdown(post.body,extensions=[
        'markdown.extension.extra',
        'markdown.extension.codehilite',
        'markdown.extension.toc'
    ])
    return render(request, 'blog/detail.html', context={'post': post})