#-*- coding:utf-8 -*-
from .forms import LoginForm,RegisterForm,SetInForm,CommentForm,SearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_page
from .models import Article,Comment,Poll,NewUser
from django.shortcuts import render,redirect
from django.http import JsonResponse
import markdown2,urlparse
###############################################################################
###############################################################################

def index(request):
	latest_article_list=Article.objects.query_by_time()
	if request.user is not None:
		u_active=True
		user_page='用户'
		content={'latest_article_list':latest_article_list,'u_active':u_active,"user":user_page}
		return render(request,'index.html',content)
	else:
		context={'latest_article_list':latest_article_list,'u_active':False}
		return render(request,'index.html',context)


def log_in(request):
	if request.method=='GET':
		url=request.META.get('HTTP_REFERER')
		request.session["source_url"]=url
		return render(request,'login.html')
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['uid']
			password=form.cleaned_data['pwd']
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				url=request.session["source_url"]
				return redirect(url)
			else:
				error=True
				return render(request,'login.html',{'error':error})
		else:
			error=True
			return render(request,'login.html',{'error':error})


###############################################################################

@login_required
def log_out(request):
	url=request.session['source_url']
	logout(request)
	return redirect(url)

###############################################################################
'''
def article(request,article_id):
	article=get_object_or_404(Article,id=article_id)
	content=markdown2.markdown(article.content,extras=['code-friendly','fenced-code-blocks','header-ids','toc','metadata'])
	commentform=CommentForm()
	loginform=LoginForm()
	comments=article.comment_set.all
	return render(request,'article_page.html',{'article':article,'loginform':loginform,
		'commentform':comment,
		'content':content,
		'comment':omments
		})

###############################################################################

@login_required
def comment(request,article_id):
	form=CommentForm(request.POST)
	url=urlparse.urljoin('/focus/',article_id)
	if form.is_valid():
		user=request.user
		article=Article.objects.get(id=aritcle_id)
		new_comment=form.cleaned_data['comment']
		c=Comment(content=new_comment,article_id=article_id)
		c.user=user
		c.save()
		article.comment_num+=1
		return direct(url)

###############################################################################

@login_required
def get_keep(request,article_id):
	logged_user=request.user
	article=Article.object.get(id=article_id)
	articles=logged_user.article_set.all()
	if article not in articles:
		article.user.add(logged_user)
		article.keep_num+=1
		article.save()
		return redirect('/focus/')
	else:
		url=urlparse.urljoin('focus/',article_id)
		return redirect(url)

###############################################################################

@login_required
def get_poll_article(request,article_id):
	logged_user=request.user
	article=Article.object.get(id=article_id)
	polls=logged_user.poll_set.all()
	articles=[]
	for poll in polls:
		articles.append(poll.article)
	if article in articles:
		url=urlparse.urljoin('/focus/',article_id)
		return redirect(url)
	else:
		article.poll_num+=1
		article.save()
		poll=Poll(user=logged_user,article=article)
		poll.save()
		data=[]
		return redirect('/focus/')

###############################################################################

def register(request):
	error1="this name already exist"
	valid='this name is valid'

	if reuqies.method=='GET':
		form=RegisterForm()
		return render(request,'register.html',{'form':form})
	if request.method=='POST':
		form=RegisterForm(request.POST)
		if request.POST.get('raw_username','erjgiqfv240hqp5668ej23foi')!='erjgiqfv240hqp5668ej23foi':
			try:
				user=NewUser.objects.get(username=request.POST.get('raw_username',''))
			except ObjectDoesNotExist:
				return render(request,'register.html',{'form':form,'msg':valid})
			else:
				return render(request,'register.html',{'form':form,'msg':error1})
		else:
			if form.is_valid():
				username=form.cleaned_data['username']
				email=form.cleaned_data['email']
				passwod1=form.cleaned_data['password1']
				password2=form.cleaned_data['password2']
				if password1!=password2:
					return render(request,'register.html',{'form':form,'msg':'two password is not equal'})
				else:
					user=NewUser(username=username,email=email,password=password1)
					user.save()
					return redirect('/focus/login')
			else:
				return render(request,'register.html',{'form':form})

'''