from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.notice_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', views.notice_detail, name='post_detail'),
]