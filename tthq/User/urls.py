from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'^info/$',views.user_input),
    url(r'^log/$',views.log),
    url(r'^jason/$',views.detection_name),
    url(r'^active(\d+)/$',views.active),
    url(r'^',views.index),
]