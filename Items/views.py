from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Items, Category
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages



def index(request):
    # req = Items.objects.all()
    #  one = Items.objects.get(pk=2)
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
    category_item = Items.objects.filter(category=category_user)
    allcate = Category.objects.all()
    dane = {'category_user': category_user,
            'category_item': category_item,
            'category': allcate}
    return render(request, 'category_item.html', dane)


def items(request, id):
    items_user = Items.objects.get(pk=id)
    allcate = Category.objects.all()
    dane = {'items_user': items_user, 'category': allcate}
    return render(request, 'item.html', dane)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("http://127.0.0.1:8000/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("http://127.0.0.1:8000/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGOUT_REDIRECT_URL, request.path))

