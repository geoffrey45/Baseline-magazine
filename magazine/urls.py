from . import views
from django.urls import include, path
from .views import article,index,signup,search_results,new_article,magazineList,update_profile,profile,filter_by_editor,apiDescription,all_editors,update_article
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	path('signup/',signup,name='signup'),
	path('',index,name='index'),
	# path('update//',update_article,name='update_article'),
	path('article/new/',new_article,name='new_article'),
	path('article/<slug:slug>/edit/',update_article,name='update_article'),
 	path('article/<slug:slug>',article,name='article'),
 	path('search/',search_results,name='search_results'),
	path('api/model/',magazineList.as_view()),
	path('api/model/item/<pk>',apiDescription.as_view()),
	path('profile/update/',update_profile,name='update_profile'),
	path('profile/',profile,name='profile'),
 	path('editor/',all_editors,name='all_editors'),
	path('editor/<username>/',filter_by_editor,name='filter_by_editor'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)