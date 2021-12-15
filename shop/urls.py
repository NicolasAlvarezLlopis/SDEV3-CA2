from os import name
from django.urls import path
from .views import ProdCat, ProdDetail

app_name = 'shop'

urlpatterns = [
    path('', ProdCat.as_view(), name='allProdCat'),
    path('<uuid:category_id>/', ProdCat.as_view(), name='products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', ProdDetail.as_view(), name = 'prod_detail'),
]

