# -*- encoding:utf-8 -*-
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
import datetime
###############################################################################
###############################################################################

@python_2_unicode_compatible
class NewUser(AbstractUser):
	profile=models.CharField('profile',default='',max_length=256)

	def __str__(self):
		return self.username

###############################################################################

@python_2_unicode_compatible
class Column(models.Model):
	name=models.CharField('column_name',max_length=256)
	intro=models.TextField('introduction',default='')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='column'
		verbose_name_plural='columns'
		ordering=['name']

###############################################################################

@python_2_unicode_compatible
class Article(models.Model):
	column=models.ForeignKey(Column,blank=True,null=True,verbose_name='belong_to')
	title=models.CharField(max_length=256)
	author=models.ForeignKey('Author')
	user=models.ManyToManyField('NewUser',blank=True)
	content=models.TextField('content')
	pub_date=models.DateTimeField(auto_now_add=True,editable=True)
	update_time=models.DateTimeField(auto_now=True,null=True)
	published=models.BooleanField('notDraft',default=True)
	poll_num=models.IntegerField(default=0)
	comment_num=models.IntegerField(default=0)
	keep_num=models.IntegerField(default=0)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='article'
		verbose_name_plural='articles'

###############################################################################

@python_2_unicode_compatible
class Comment(models.Model):
	user=models.ForeignKey('NewUser',null=True)
	article=models.ForeignKey(Article,null=True)
	content=models.TextField()
	pub_date=models.DateTimeField(auto_now_add=True,editable=True)
	poll_num=models.IntegerField(default=0)

	def __str__(self):
		return self.content

###############################################################################

@python_2_unicode_compatible
class Author(models.Model):
	name=models.CharField(max_length=256)
	profile=models.CharField('profile',default='',max_length=256)
	register_date=models.DateTimeField(auto_now_add=True,editable=True)

	def __str__(self):
		return self.name

###############################################################################

class poll(models.Model):
	user=models.ForeignKey('NewUser',null=True)
	article=models.ForeignKey(Article,null=True)
	comment=models.ForeignKey(Comment,null=True)



