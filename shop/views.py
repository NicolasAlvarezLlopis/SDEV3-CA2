from django.core import paginator
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView, DetailView
from django.core.paginator import Page, Paginator, EmptyPage, InvalidPage
from django.views.generic import TemplateView

class ProdDetail(DetailView):
    model = Product

    def get(self, request, category_id, product_id):
        try:
            product = Product.objects.get(category_id = category_id, id = product_id)
        except Exception as e:
            raise e
        return render(request, "shop/product.html",{'product':product})



class ProdCat(ListView):
    model = Product

    def get(self,request, category_id=None):
        category = None
        products = None
        if category_id != None:
            category = get_object_or_404(Category, id = category_id)
            products = Product.objects.filter(category = category, available = True)
        else:
            products = Product.objects.all().filter(available = True)
        
        paginator = Paginator(products, 6)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            products = paginator.page(page)
        except (EmptyPage, InvalidPage):
            products = paginator.page(paginator.num_pages)
        
        return render(request, "shop/category.html",{'category':category, 'products':products})

def about(request):
    return render(request, 'about.html')