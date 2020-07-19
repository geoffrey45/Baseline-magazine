from . import views
from django.urls import include, path
from .views import article,index,signup,search_results,magazineList,update_profile,profile,filter_by_editor,apiDescription,all_editors,update_article,delete_article,new_article,delete_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	path('signup/',signup,name='signup'),
	path('',index,name='index'),
	path('article/new/<username>',new_article,name='new_article'),
  	path('article/<slug:slug>',article,name='article'),
	path('article/<slug:slug>/edit/',update_article,name='update_article'),
	path('article/<slug:slug>/delete',delete_article,name='delete_article'),
 	path('search/',search_results,name='search_results'),
	path('api/model/',magazineList.as_view()),
	path('api/model/item/<pk>',apiDescription.as_view()),
 	path('profile/<username>',profile,name='profile'),
	path('profile/<username>/update/',update_profile,name='update_profile'),
  	path('profile/<pk>/delete',delete_user,name='delete_user'),
 	path('editor/',all_editors,name='all_editors'),
	path('editor/<username>/',filter_by_editor,name='filter_by_editor'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)