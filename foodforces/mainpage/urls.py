from django.conf.urls import url
from . import views

app_name='mainpage'

urlpatterns=[
    #/mainpage/
    url(r'^$',views.index,name='index'),
    
    #/mainpage/<order_id>
    url(r'^(?P<pk>[0-9]+)/$',views.detail.as_view(),name='detail'),

    #/mainpage/add_order
    url(r'^addorder/$',views.add_order.as_view(),name='add-order'),
    #/mainpage/<order_id>/delete
    url(r'^(?P<pk>[0-9]+)/delete/$',views.orderDeleteView.as_view(),name='delete-order'),
]
