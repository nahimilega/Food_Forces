from django.conf.urls import url
from . import views

urlpatterns=[
    #/mainpage/
    url(r'^$',views.index,name='index'),
    
]
