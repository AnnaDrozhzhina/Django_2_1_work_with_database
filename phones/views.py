from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    template = 'catalog.html'
    select = {'name': 'name',
              'min_price': 'price',
              'max_price': '-price'
              }
    sort = request.GET.get('sort')
    if sort:
        phones = phones.order_by(select[sort])
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    context = {'phones': Phone.objects.get(slug=slug)}
    return render(request, template, context)
