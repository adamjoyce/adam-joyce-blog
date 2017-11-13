from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^archive/$', views.archive, name='archive_all'),
    url(r'^(?P<category_slug>)', views.archive, name='archive_category'),
]
