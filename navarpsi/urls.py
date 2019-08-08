from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^user/', include('User.urls')),
    url(r'^accounts/', include('session.urls')),
]
