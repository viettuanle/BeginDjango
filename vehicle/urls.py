from django.conf.urls import url
from vehicle import  views
urlpatterns = [
   url(r'^display/$', view= views.display),
]