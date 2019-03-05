from django.conf.urls import url
from django.contrib import admin
from post import views


app_name='post'

urlpatterns=[
    url(r'^$',views.post_list, name='list'),

    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$',views.post_detail, name='detail'),
    url(r'^create/$',views.post_create, name='create'),

    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/edit/$',views.post_update, name='update'),
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/delete/$',views.post_delete, name='delete'),

    url(r'^aboutus/$', views.about, name='about'),
    url(r'^contactus/$', views.contact, name='contact'),
    url(r'^contactus/completed/$', views.completed, name='completed'),

    url(r'^readme/$', views.readme, name='readme'),

]