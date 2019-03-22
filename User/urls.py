from django.conf.urls import include, url
from . import views
# from django.contrib.auth.views import login

urlpatterns = [
    url('filter/', views.filterPatient, name='filterPatient'),
    url('create/patient/', views.createPatient, name='createPatient'),
    url('create/', views.createF01, name='createF01'),
    url('detail/(?P<pk>[0-9]+)/', views.detailF01, name='detailF01'),
    url('board/', views.board, name='board'),
]