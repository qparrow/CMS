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
	loginform=LoginForm()
	context={'latest_article_list':latest_article_list,'loginform':loginform}
	return render(request,'index.html',context)


def log_in(request):
	if request.method=='GET':
		form=LoginForm()
		return render(request,'login.html',{'form':form})
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['uid']
			password=form.cleaned_data['pwd']
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				url=request.POST.get('source_url','/focus')
				return redirect(url)
			else:
				return render(request,'login.html',{'form':form,'error':"password or username is not true!"})
		else:
			return render(request,'login.html',{'form':form})

###############################################################################
@login_required
def log_out(request):
	url=request.POST.get('source_url','/focus/')
	logout(request)
	return redirect(url)


