from django.shortcuts import render
from .models import user, order
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views import generic

def index(request):
    
    all_user=user.objects.all()
    all_order=order.objects.all()
    a={
      'all_user':all_user,
      'all_order':all_order,
    }

    return render(request,"index.html",a)
    
'''
def detail(request,order_id):
	selected_order=order.objects.get(pk=order_id)
	a={
      'selected_order':selected_order,
    }
	return render(request,"detail.html",a)



class IndexView(generic.ListView):
    template_name="music/index.html"
    context_object_name="all_albums"
    def get_queryset(self):
        return Album.objects.all()
'''
class detail(generic.DetailView):
    model=order
    template_name="detail.html"



class add_order(CreateView):
	model=order
	fields=['resturant_name','offer_description','Target_value']


class orderDeleteView(DeleteView):
    model = order
    success_url = reverse_lazy('mainpage:index')
