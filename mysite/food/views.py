from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Place

# class StoreListView(generic.ListView):
#     model = Store
#     context_object_name = 'store_list'
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get the context
#         context = super(StoreListView, self).get_context_data(**kwargs)
#         # Create any data and add it to the context
#         context['some_data'] = 'This is just some data'
#         return context


# Create your views here.
def index(request):
    # return HttpResponse("Hello food!")
    return render(request, 'food/index.html', {'store_list': Place.objects.all(), }
                  )
