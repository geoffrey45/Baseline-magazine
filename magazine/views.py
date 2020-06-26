from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from .models import Article,NewsLetterRecipients
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewArticleForm
from .email import send_welcome_mail
from tinymce.models import HTMLField
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import magazineApiModel
from .serializer import apiSerializer
from rest_framework import status
from .permissions import IsAuthenticatedOrReadOnly

def index(request):
    date = dt.date.today()
    articles = Article.all_articles()
    return render(request,'index.html',{'articles': articles})
# def newsletter(request):
#     name = request.POST.get('your_name')
#     email = request.POST.get('email')

#     recipient = NewsLetterRecipients(name=name,email=email)
#     recipient.save()
#     send_welcome_mail(name,email)
#     data = {'success':'You have been successfully added to mailing list'}
#     return JsonResponse(data)

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

@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid(): 
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('index')

    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form": form})

class magazineList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def post(self,request,format=None):
        serializers = apiSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,format=None):
        all_items = magazineApiModel.objects.all()
        serializers = apiSerializer(all_items,many=True)
        return Response(serializers.data)

class apiDescription(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_item(self,pk):
        try:
            return magazineApiModel.objects.get(pk=pk)
        except magazineApiModel.DoesNotExist:
            return Http404
    
    def get(self,request,pk,format=None):
        item = self.get_item(pk)
        serializers = apiSerializer(item)
        return Response(serializers.data)

    def put(self,request,pk,format=None):
        item = self.get_item(pk)
        serializers = apiSerializer(item,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format = None):
        item = self.get_item(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)