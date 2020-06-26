from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^article/(\d)',views.article,name='article'),
	url(r'^search/',views.search_results,name='search_results'),
	url(r'new/article/$',views.new_article,name='new_article'),
	# url(r'^ajax/newsletter/$',views.newsletter,name='newsletter'),
	url(r'^api/model/$',views.magazineList.as_view()),
	url(r'api/model/item-id/(?P<pk>[0-9]+)/$',views.apiDescription.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
