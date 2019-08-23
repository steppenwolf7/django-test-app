from django.shortcuts import render
from .models import Products
from .forms import ProductsForm, RawProductForm
# Create your views here.

def product_detail_view(request):
    obj = Products.objects.get(id=4)
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









# def product_create_view(request):
#     form = ProductsForm(request.POST or None)
#     if form.is_valid():
#        form.save()
#        form =ProductsForm()

#     context = { 
#       'form': form
#     }      
#     return render(request, "product/product_create.html", context)    