from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^treenodes/$', views.TreeNodeList.as_view()),
    url(r'^treenodes/(?P<pk>[0-9]+)/$', views.TreeNodeDetail.as_view()),
    url(r'^fetchChildren/$', views.fetchChildren),
    url(r'^tempView/$', TemplateView.as_view(template_name = "hotspots/nigs.html")),
    url(r'^$', TemplateView.as_view(template_name = "hotspots/index.html"))
]

urlpatterns = format_suffix_patterns(urlpatterns)