from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Article
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist

def index(request):
	date = dt.date.today()
	articles = Article.all_articles()
	return render(request,'index.html',{'articles': articles})

def article(request,article_id):
	try:
		article = Article.objects.get(id = article_id)
	except ObjectDoesNotExist:
		raise Http404()
	return render(request,'article.html',{'article':article})