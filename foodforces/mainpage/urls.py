from django.conf.urls import url
from . import views

urlpatterns=[
    #/music/
    url(r'^$',views.index,name='index'),
    
]
