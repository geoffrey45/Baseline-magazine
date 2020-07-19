from django.contrib.auth.views import LogoutView
from django.urls import path,include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('magazine.urls')),
    path('accounts/', include('registration.backends.simple.urls'),{'next_page':'/'}),
    path('logout/',LogoutView.as_view(),{'next_page':'/'}),
    path('summernote/',include('django_summernote.urls')),
    path('api/token-auth/',obtain_auth_token),
]
