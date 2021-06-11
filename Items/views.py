from django.shortcuts import render
from django.http import HttpResponse
from .models import Items, Category


# Create your views here.


def index(request):
    # req = Items.objects.all()
    # one = Items.objects.get(pk=2)
    # cate = Items.objects.filter(category=5)
    # crea = Items.objects.filter(creator=1)
    # cate_name = Category.objects.get(id=1)
    allcate = Category.objects.all()
    # null = Items.objects.filter(category__isnull=True)
    # includes = Items.objects.filter(statistics__icontains='defense')
    dane = {'category': allcate}
    return render(request, 'templates1.html', dane)


def category(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user.name)


def items(request, id):
    items_user = Items.objects.get(pk=id)
    allcate = Category.objects.all()
    dane = {'items_user': items_user, 'category': allcate}
    return render(request, 'item.html', dane)
