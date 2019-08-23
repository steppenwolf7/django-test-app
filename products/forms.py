from django import forms
from .models import Products

class ProductsForm(forms.ModelForm): 
    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title"}))   
    description = forms.CharField(required=False, widget=forms.Textarea())
    price       = forms.DecimalField(initial=99.99)