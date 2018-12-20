from django.conf.urls import url
from . import views

app_name='landingpage'

urlpatterns=[
    
    url(r'^$',views.index,name='ind'),

]
