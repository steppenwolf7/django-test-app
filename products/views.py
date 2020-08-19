from django.shortcuts import render, get_object_or_404 #redirect 
from .models import Products
from .forms import ProductsForm
from django.views.generic import (
  CreateView
)
#from django.urls import reverse
#from django.http import Http404




def product_detail_view(request,id):
    obj =  get_object_or_404(Products, id=id)
    context = {
        'object': obj
    }                                                          #return redirect('../../')
    return render(request, "product/detail.html", context) 
    
                                                              
def product_create_view(request):    
    form = RawProductForm()
    if request.method == "POST":
      form = RawProductForm(request.POST)
      if form.is_valid():
        print(form.clean_data)
        Products.objects.create(**form.cleaned_data)
      else:
        print(form.errors)
    context = {
      'form': form
    }
    return render(request, "product/product_create.html", context)

class ProductCreateView(CreateView):
    template_name = 'product/product_class_create.html'
    form_class = ProductsForm
    queryset = Products.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)





def product_list_view(request):
    queryset = Products.objects.all()              # geting list of objects 
    context = {
      "object_list": queryset
     }
    return render(request, "product/product_list.html", context)




# def product_create_view(request):
#     form = ProductsForm(request.POST or None)
#     if form.is_valid():
#        form.save()
#        form =ProductsForm()

#     context = { 
#       'form': form
#     }      
#     return render(request, "product/product_create.html", context)    
#try:
  
  
# product_detail_view  
#   obj = Products.objects.get(id=id)
#except Products.DoesNotExist:
#   raise Http404
#context = {
#   'title': obj.title,
#  'description': obj.description
                                                            
# def product_create_view(request):