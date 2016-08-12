# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone

# 7)
from .models import Post, Comment


# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-published_date') # old items first, negative sorting 
    user = request.user
    context = {'posts': posts, 'current_user': user,}
    return render(request, 'blog/index.html', context)


# 8)
# making Templates folder
# Templates > app name folder
# make index.html 



# form 태그의 submit 를 통해 action을 향해 method(POST)를 날릴 경우,
# 장고가 전달/요청에 따라 request 객체(object) 를 만들어준다.
def write(request):
    post = Post()
    post.author = request.user
    # print(request.user) -> repositivator 가 출력된다 : admin 에 로그인한 id 인듯 
    post.title = request.POST['title']
    post.text = request.POST['text']
    post.published_date = timezone.now()
    post.save()
    
    # return redirect('blog.views.index')
    return redirect('index')
    
    
# 아래와 같이 request 외에 다른 인자를 받아올 경우 : GET 방식 

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    
    return redirect('index')
    
    
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":                # POST 
        post.author = request.user
        post.title = request.POST['title']
        post.text = request.POST['content']
        post.published_date = timezone.now()
        post.save()
        return redirect('index')
    else:
        context={'post' : post}                 # GET (삭제 전에 먼저 해당 post 를 담아주는 것)
        return render(request, 'blog/post_edit.html', context)
        
        
def reply_write(request):
    
    comment = Comment() # Comment() 객체 생성 
    
    # Comment는 비록 post라는 attribute를 가지지만 
    # Post 모델의 인스턴스와 1:N의 관계를 맺으려면 'post' 대신에 '_id'를 덧붙여서 post_id 즉 primary key를 통해 관계를 맺을 수 있다.
    # comment 가 속한 post의 id 를 지정해주는 것 
    comment.post_id = request.POST['id_of_post']
    # Comment 클래스의 [ post = models.ForeignKey('blog.Post', related_name='comments') ] 변수에 id_of_post 를 매겨주는 것 
    
    comment.author = request.user
    comment.text = request.POST['content']
    comment.save()
    return redirect('index')
    
    
    
def reply_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    
    return redirect('index')