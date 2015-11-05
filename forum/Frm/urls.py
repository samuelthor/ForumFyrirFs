from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /frm/
    url(r'^$', views.index, name='index'),
    # ex: /frm/5/
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /frm/5/results/
    url(r'^(?P<post_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /frm/5/vote/
    url(r'^(?P<post_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
