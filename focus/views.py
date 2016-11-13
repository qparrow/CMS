from .forms import CommentForm,LoginForm,RegisterForm,SetInfoForm,SearchForm
from django.contrib.auth.decorators import login_required
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
	loginform=loginForm()
	context={'latest_article_list':latest_article_list,'loginform':loginform}
	return render(request,'index.html',context)

###############################################################################


