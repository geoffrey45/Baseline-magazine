from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Article,NewsLetterRecipients
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm
from .email import send_welcome_mail

def index(request):
    date = dt.date.today()
    articles = Article.all_articles()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_mail(name,email)

            HttpResponseRedirect('news_today')

    return render(request,'index.html',{'articles': articles,'letterform':form})

@login_required(login_url='/accounts/login/')
def article(request,article_id):
	try:
		article = Article.objects.get(id = article_id)
	except ObjectDoesNotExist:
		raise Http404()
	return render(request,'article.html',{'article':article})

def search_results(request):
	if 'q' in request.GET and request.GET['q']:
		search_term = request.GET.get('q')
		searched_articles = Article.search(search_term)
		message = f'{search_term}'
		return render(request,'search.html',{'message':message,'articles':searched_articles})
	else:
		message = 'Why? Just why!'
		return render(request,'search.html',{'message':message})

