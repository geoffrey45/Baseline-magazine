from django.contrib.auth import views
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('magazine.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls'),{'next_page':'/'}),
    url(r'^logout/$',views.logout,{'next_page':'/'}),
]

