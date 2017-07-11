from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^/$', views.post_list, name="post_list"),
    url(r'^/stuff/$', views.post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^post/$', views.new_post, name='new_post'),
]