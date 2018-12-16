from django.shortcuts import render
from .models import user, order


def index(request):
    
    all_user=user.objects.all()
    a={
      'all_user':all_user,
    }

    return render(request,"index.html",a)
    

