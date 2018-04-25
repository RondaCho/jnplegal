from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lawyer_list, name='lawyer_list'),
    #url(r'^(?P<id>[A-Za-z0-9]+)/$', views.lawyer_detail, name='lawyer_detail'),
    url(r'^(?P<slug>[-\w]+)/$', views.lawyer_detail, name='lawyer_detail'),
]