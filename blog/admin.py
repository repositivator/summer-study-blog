# coding: utf-8

from django.contrib import admin


# 11)
from .models import Post

# Register your models here.
admin.site.register(Post)


# 11-2) 
# python manage.py createsuperuser 



# 12) 한글주석처리 시 
# 최상단에 적어주기 : [ # coding: utf-8 ]
