"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^types/$', views.types, name='types'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^types/(?P<type_id>\d+)/$', views.type, name='type'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    url(r'^entry/(?P<entry_id>\d+)/$', views.entry, name='entry'),
    url(r'^entry/(?P<entry_id>\d+)/add_to_fav/$', views.add_to_fav, name='add_to_fav'),
    url(r'^entry/(?P<entry_id>\d+)/remove_from_fav/$', views.remove_from_fav, name='remove_from_fav'),
    url(r'^favourites/$', views.favourites, name='favourites'),
    url(r'edit_comment/(?P<entry_id>\d+)/(?P<comment_id>\d+)/$', views.edit_comment, name='edit_comment'),
    url(r'delete_entry/(?P<topic_id>\d+)/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry'),

]
