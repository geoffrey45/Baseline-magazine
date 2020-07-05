from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from .models import mode,Editor,Profile,Comment,magazineApiModel
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import NewArticleForm, SignUpForm,UserUpdateForm,ProfileUpdateForm,CommentForm
from .email import send_welcome_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import apiSerializer
from rest_framework import status
from .permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            
            # name = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # send_welcome_mail(name,email)
            
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

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
        
def index(request):
    articles = mode.all_articles().order_by('-created_on')
    paginator = Paginator(articles,3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'page':page,'articles':articles})

def search_results(request):
    if 'q' in request.GET and request.GET['q']:
        search_term = request.GET.get('q')
        articles = mode.search(search_term).order_by('-created_on')

        return render(request,'article/search.html',{'search_term':search_term,'articles':articles})
    else:
        message = 'Why? Just why!'
        return render(request,'article/search.html',{'message':message})

@login_required(login_url='/accounts/login/')
def new_article(request,username):
    current_user = request.user
    username = current_user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('index')

    else:
        form = NewArticleForm()
    return render(request, 'article/new_article.html', {"form": form})

def article(request, slug):
    post = mode.objects.get(slug = slug)
    template_name = 'article/article.html'
    # post = get_object_or_404(mode,id = article_id)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():

            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()

    return render(request, template_name, {'post': post, 'comments': comments,'new_comment': new_comment,'form': form})

def filter_by_editor(request,username):
    articles = mode.objects.filter(editor__username=username).order_by('-created_on')
    username = mode.objects.filter(editor__username=username).order_by('-created_on').first()
    return render(request,'article/sort.html',{'articles':articles,'username':username})

def all_editors(request):
    editors = Profile.all_editors()
    return render(request,'article/all.html',{'editors':editors})

@login_required(login_url='/accounts/login/')
def update_article(request,slug):
    instance = get_object_or_404(mode,slug=slug)
    form = NewArticleForm(request.POST or None,request.FILES or None, instance = instance)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'article/update.html',{'form':form})

@login_required(login_url='/accounts/login')
def delete_article(request,slug):
    instance = get_object_or_404(mode,slug=slug)
    instance.delete()
    return redirect('/')

@login_required(login_url='/accounts/login/')
def update_profile(request,username):
    username = request.user.username
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('index')
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':user_form,
        'p_form':profile_form
        }

    return render(request,'profile/update.html',context)

@login_required(login_url='/accounts/login')
def delete_user(request,pk):
    instance = request.user
    instance.delete()
    return redirect('/')

@login_required(login_url='/accounts/login/')
def profile(request,username):
    user = request.user
    username = user.username
    return render(request,'profile/profile.html',{'user':user})
