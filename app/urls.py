from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
#	from .views import StudentViewSet, UniversityViewSet

from . import views

urlpatterns = [
    url(r'^app/$', views.Check),
    url(r'^app/getUser/', views.getUser),
    url(r'^app/addUser/', views.addUser),
    url(r'^app/logout/',views.logout1),
   # url(r'^tes/(?P<pk>[0-9]+)/$', views.snippet_detail),
    #url(r'^authors/$', views.AuthorView.as_view(), name='author-list'),
]
