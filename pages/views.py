import runpy, sys
import this  
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request, *args, **kwargs):
    python =  { 
        "zen": dir(this)
                }
    return render(request, "home.html", python)

def about(request, *args, **kwargs):
    return render(request, "about.html", {})

def contact(request, *args, **kwargs):
    dictionary = {
        "kay": "value",
        "klucz": "wartość",
        "list": [123, 123, 123, 345]
     }
    return render(request, "contact.html", dictionary)    


print()