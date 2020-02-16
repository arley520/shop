from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^book/$', views.BookView.as_view()),
    # url(r'^book/(?P<id>\d+)/$', views.BookEditView.as_view()),
    url(r'^book/$', views.BookModelView.as_view({"get": "list", "post": "create"})),
    url(r'^book/(?P<pk>\d+)/$', views.BookModelView.as_view({"get": "retrieve", "post": "update", "delete": "destroy"})),
]
