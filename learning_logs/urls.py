from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url('^topics/$', views.topics, name='topics'),
        url('^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
        url('^new_topic/$', views.new_topic, name='new_topic'),
        url('^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
        url('^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
        ]
