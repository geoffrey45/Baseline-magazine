from django.contrib.auth.views import LogoutView
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('magazine.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls'),{'next_page':'/'}),
    url(r'^logout/$',LogoutView.as_view(),{'next_page':'/'}),
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^api/token-auth/',obtain_auth_token),
]
