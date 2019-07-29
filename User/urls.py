from django.conf.urls import include, url
from . import views
# from django.contrib.auth.views import login

urlpatterns = [
    url('filter/patiente/', views.filterPatient, name='filterPatient'),
    url('filter/role/', views.filterRole, name='filterRole'),
    url('create/patient/', views.createPatient, name='createPatient'),
    url('create/requeriments/(?P<case>[0-9]+)/(?P<package>[0-9]+)', views.createRequeriments, name='createRequeriments'),
    url('create/', views.createF01, name='createF01'),
    url('detailF01/(?P<case>[0-9]+)/(?P<package>[0-9]+)', views.detailF01, name='detailF01'),
    url('detail/', views.detailUser, name='detailUser'),
    url('board/', views.board, name='board'),
]