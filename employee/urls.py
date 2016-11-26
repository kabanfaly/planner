from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.index),
    url(r'view/(?P<id>\d+)^$', views.show),

]
