# coding: utf-8

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    
    url(r'^write/$', views.write, name = 'write'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name = 'delete'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name = 'edit'),
    
    url(r'^reply_write/$', views.reply_write, name='reply_write'),
    url(r'^reply/(?P<pk>\d+)/delete/$', views.reply_delete, name='reply_delete'),
]

# r : 정규표현식의 시작
# ^ : 그 앞에 문자가 오지 않는다는 의미
# pk : get 방식으로 넘겨줄 때의 이름 
# \d : <~> 자리에 숫자만 올 수 있다고 지정해주는 것
# + : 글자 수를 한정해준다 
# $ : 이 뒤에 아무것도 오지 않는다는 의미
