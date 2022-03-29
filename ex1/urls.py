from django.urls import path
from . import views #현재경로에서 views.py 임포트 하겠다.

urlpatterns=[
    path('', views.index, name='index'),
]