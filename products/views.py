from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Product
from .forms import ProductAddForm,ProductModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from digitalmarket.mixins import MultiSlugMixin,SubmitBtnMixin
from django.views.generic.edit import CreateView,UpdateView
# Create your views here.

class ProductCreateView(SubmitBtnMixin,CreateView):
    model = Product
    template_name="form.html"
    form_class = ProductModelForm
    success_url = "/products/add/"
    submit_btn = "Add Product"

class ProductUpdateView(SubmitBtnMixin,MultiSlugMixin,UpdateView):
    model = Product
    template_name="form.html"
    form_class = ProductModelForm
    success_url = "/products/"
    submit_btn = "Update Product"

class ProductDetailView(MultiSlugMixin,DetailView):
    model = Product

class ProductListView(ListView):
    model = Product

    def get_queryset(self,*args,**kwargs):
        qs = super(ProductListView,self).get_queryset(**kwargs)
        return qs.filter(title__icontains="deneme")

def create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()
    template="form.html"
    context={
    'form':form,
    'submit_btn':'Create Product',
    }
    return render(request,template,context)

def update_view(request,object_id=None):
    product = get_object_or_404(Product, id=object_id)
    form = ProductModelForm(request.POST or None,instance=product)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.sale_price = instance.price
        instance.save()
    template="form.html"
    context={
        'object':product,
        'form':form,
        'submit_btn':'Update Product',
        }
    return render(request,template,context)

def detail_slug_view(request,slug=None):
    product = Product.objects.get(slug=slug)
    try:
        product = get_object_or_404(Product,slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by('-title').first()
    template="detail_view.html"
    context={
        'object':product,
        }
    return render(request,template,context)

def detail_view(request,object_id=None):
    product = get_object_or_404(Product, id=object_id)
    template="detail_view.html"
    context={
        'object':product,
        }
    return render(request,template,context)

def list_view(request):
    queryset = Product.objects.all()
    template="list_view.html"
    context={
    'queryset':queryset,
    }

    return render(request,template,context)
