from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^archive/$', views.archive, name='archive_all'),
    url(r'^random-post/(?P<random>.+)/$', views.post, name='random_post'),
    url(r'^(?P<category_slug>.+)/(?P<post_slug>.+)/$', views.post, name='post'),
    url(r'^(?P<category_slug>.+)/$', views.archive, name='archive_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
