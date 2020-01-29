from django.shortcuts import render, get_object_or_404 #redirect 
from .models import Products
from .forms import ProductsForm, RawProductForm
#from django.http import Http404

def product_detail_view(request,id):
    
    obj =  get_object_or_404(Products, id=id)
      #return redirect('../../')
    
    
    #try:
    #   obj = Products.objects.get(id=id)
    #except Products.DoesNotExist:
    #   raise Http404
    context = {
        'object': obj
    } 
                                                          #context = {
                                                        #   'title': obj.title,
                                                           #  'description': obj.description
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


def product_list_view(request):
    number = 1
    queryset = Products.objects.all()              # geting list of objects 
    context = {"object_list": queryset, "numberone": number}
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