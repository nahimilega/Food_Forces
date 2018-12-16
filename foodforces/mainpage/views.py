from django.shortcuts import render
from .models import user, order


def index(request):
    
    all_user=user.objects.all()
    all_order=order.objects.all()
    a={
      'all_user':all_user,
      'all_order':all_order,
    }

    return render(request,"index.html",a)
    

