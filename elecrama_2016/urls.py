from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from bedroom import views_new


urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^bedroom/$', views_new.bedroomList.as_view()),
    url(r'^bedroom/(?P<pk>[0-9]+)/$', views_new.bedroomDetail.as_view()),   
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)



