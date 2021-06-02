from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .forms import UserForm, SearchForm
from .models import Product

# Create your views here.

def main(request):
    news = Product.objects.filter(special__icontains="new")[:3]
    bests = Product.objects.filter(special__icontains="best")[:3]
    context = {
        'news' : news,
        'bests' : bests
    }
    return render(request, 'page/main.html', context)

def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect(request, 'page/main.html')
    else:
        form = UserForm()
    return render(request, 'page/join.html')

def login(request):
    return render(request, 'page/login.html')

def logout(request):
    return render(request, 'page/main.html')

def cart(request):
    return render(request, 'page/cart.html')

def mypage(request):
    return render(request, 'page/mypage.html')

def result(request):
    search = request.GET.get('searchstr')
    results = Product.objects.filter(title__icontains=search)
    context = {
        'searchstr' : search,
        'products' : results
    }
    return render(request, 'page/result.html', context)

def howto(request):
    return render(request, 'page/howto.html')

def new(request):
    results = Product.objects.filter(special__icontains="new")
    context = {
        'products' : results
    }
    return render(request, 'page/shop/shopnew.html', context)

def best(request):
    results = Product.objects.filter(special__icontains="best")
    context = {
        'products' : results
    }
    return render(request, 'page/shop/shopbest.html', context)

def nail(request):
    results = Product.objects.filter(category__icontains="nail")
    context = {
        'products' : results
    }
    return render(request, 'page/shop/shopnail.html', context)

def pedi(request):
    results = Product.objects.filter(category__icontains="pedi")
    context = {
        'products' : results
    }
    return render(request, 'page/shop/shoppedi.html', context)

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product' : product
    }
    return render(request, 'page/shop/shopdetail.html', context)


def event(request):
    return render(request, 'page/event.html')

def faq(request):
    return render(request, 'page/faq.html')

def location(request):
    return render(request, 'page/location.html')