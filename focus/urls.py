from django.conf.urls import include ,url
from . import views

urlpatterns=[
	url(r'^$',view.index,name='index'),
]