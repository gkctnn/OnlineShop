from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Product
from .forms import ProductAddForm
# Create your views here.

def create_view(request):
    # FORM
    form = ProductAddForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        # new_object = Product.objects.create(title=title,description=description,price=price)
        new_object = Product()
        new_object.title = title
        new_object.description = description
        new_object.price = price
        new_object.save()
    template="create_view.html"
    context={
    'form':form,
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
