from django.urls import path, re_path
from django.conf.urls import include, url
from . import views
urlpatterns = [
    #path('', views.index)
    url(r'^$', views.index),
    #re_path(r'.*', views.index)
    # match all other pages
    #url(r'^(?:.*)/?$', views.index),
]
