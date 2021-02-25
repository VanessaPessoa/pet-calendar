from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pets/$', views.PetList.as_view(), name='music-list'),

]