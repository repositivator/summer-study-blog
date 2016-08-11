# coding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 6)
from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey('auth.User')

    title = models.CharField(max_length=200)
    text = models.TextField(null=False)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title


# from django.utils import timezone
# timezone.now()
# -> 현재 지정된 timezone 의 시간을 가져온다

# import datetime
# datetime.datetime.now() 
# -> (maybe) 현재 머신 시스템의 시간을 가져온다




# 6) 
# python manage.py makemigrations blog
# python manage.py migrate




class Comment(models.Model):

    post = models.ForeignKey('blog.Post', related_name='comments')
    # post 변수에는 comment(N)들이 연결된 post(1)의 id 값이 저장된다 (commment 자체의 id 는 자체적으로 생성됨)
    # 1-1) related_name은 1:N의 관계에서 1의 모델이 N의 모델을 부를때 사용할 attribute ("post.commments.all")
    # 1-2) related_name : Post 의 comment 들을 불러내는 이름 
    # 1-3) -> posts = Post.objects.all() 로 전체 posts 들만 넘겨받은 template(index.html) 에서 "post.comments.all" 로 불러낼 수 있게 된다 
    # 2) blog.Post : 앱 이름을 함께 적어줘야 한다 (나중에 많이 연결될 수 있으므로)
         
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
        

        
        
        
        