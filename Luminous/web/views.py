from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .forms import UserForm
from .models import Product, Cart, Like
from django.core.exceptions import ObjectDoesNotExist

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
            return render(request, 'page/login.html')
    else:
        form = UserForm()
    return render(request, 'page/join.html', {'form': form})

def login(request):
    return render(request, 'page/login.html')

def logout(request):
    return render(request, 'page/main.html')

def cart(request):
    userID = request.user.id
    results = Cart.objects.filter(userID__icontains=userID)
    subtotal = 0
    total = 0
    for result in results:
        subtotal += (int(result.product.price) * int(result.quantity))
    total = subtotal + 3
    context = {
        'products' : results,
        'subtotal' : subtotal,
        'total' : total
    }
    return render(request, 'page/cart.html', context)

def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart_item = Cart.objects.get(userID=request.user.id, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except Cart.DoesNotExist:
        cart_item = Cart.objects.create(
            userID=request.user.id,
            product = product,
            quantity = 1
        )
        cart_item.save()
    return redirect('detail', product_id)
    

def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cartdelete = Cart.objects.get(userID=request.user.id, product=product)
    cartdelete.delete()

    return redirect('detail', product_id)

def cart_buy(request):
    userID = request.user.id
    results = Cart.objects.filter(userID__icontains=userID)
    for result in results:
        result.delete()

    return redirect('cart')

def mypage(request):
    return render(request, 'page/mypage.html')

def like(request):
    userID = request.user.id
    results = Like.objects.filter(userID__icontains=userID)
    context = {
        'products' : results
    }
    return render(request, 'page/like.html', context)


def like_add(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        like_item = Like.objects.get(userID=request.user.id, product=product)
        like_item.save()
    except Like.DoesNotExist:
        like_item = Like.objects.create(
            userID=request.user.id,
            product = product
        )
        like_item.save()

    return redirect('detail', product_id)
    

def like_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    likedelete = Like.objects.get(userID=request.user.id, product=product)
    likedelete.delete()

    return redirect('detail', product_id)

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

def care(request):
    results = Product.objects.filter(category__icontains="care")
    context = {
        'products' : results
    }
    return render(request, 'page/shop/shopcare.html', context)

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    liked = 0
    try:
        like_item = Like.objects.get(userID=request.user.id, product=product)
        liked = 1
    except Like.DoesNotExist:
        liked = 0

    context = {
        'product' : product,
        'liked' : liked
    }
    return render(request, 'page/shop/shopdetail.html', context)


def event(request):
    return render(request, 'page/event.html')

def faq(request):
    return render(request, 'page/faq.html')

def location(request):
    return render(request, 'page/location.html')

def result(request):
    search = request.GET.get('searchstr')
    results = Product.objects.filter(title__icontains=search)
    context = {
        'searchstr' : search,
        'products' : results
    }
    return render(request, 'page/result.html', context)