from django.urls import path
from .views import (
    product_detail_view,
    product_create_view,
    product_list_view,
    ProductCreateView,

)
app_name = 'products'
urlpatterns = [
    path('<int:id>/', product_detail_view, name='detail'),
    path('product_create/', product_create_view, name='create'),
    path('', product_list_view, name='list'),
    path('create_by_class/', ProductCreateView.as_view(), name='product_class-create'),
]
