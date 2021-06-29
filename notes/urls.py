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
app_name = "notes"

urlpatterns = [
       url(r'^$', views.notes, name='notes'),
       url(r'^(?P<note_id>\d+)/$', views.note, name='note'),
       url(r'^new_note/$', views.new_note, name='new_note'),
       url(r'^edit_note/(?P<note_id>\d+)/$', views.edit_note, name='edit_note'),
       url(r'^delete_note/(?P<note_id>\d+)/$', views.delete_note, name='delete_note'),



       #url(r'^entry/(?P<entry_id>\d+)/$', views.entry, name='entry'),
       #url(r'^entry/(?P<entry_id>\d+)/add_to_fav/$', views.add_to_fav, name='add_to_fav'),
       #url(r'^entry/(?P<entry_id>\d+)/remove_from_fav/$', views.remove_from_fav, name='remove_from_fav'),
       #url(r'^favourites/$', views.favourites, name='favourites'),
       #url(r'edit_comment/(?P<entry_id>\d+)/(?P<comment_id>\d+)/$', views.edit_comment, name='edit_comment'),

]
