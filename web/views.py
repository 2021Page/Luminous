from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .forms import *
from django.contrib.auth.models import User as django_user
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def main(request):
    news = Product.objects.filter(detail_category__icontains="new")[:3]
    bests = Product.objects.filter(detail_category__icontains="best")[:3]

    context = {
        'news' : news,
        'bests' : bests
    }
    return render(request, 'page/main.html', context)

def join(request):
    if request.method == "POST":
        joinform = JoinForm(request.POST, request.FILES)
        userform = UserForm(request.POST, request.FILES)
        print("\n\n", joinform.is_valid(), " ", userform.is_valid(), "\n\n")
        if joinform.is_valid():
            username = joinform.cleaned_data.get('username')
            raw_password = joinform.cleaned_data.get('password1')
            new_user = User.objects.create(
            user_id = username,
            password = raw_password,
            user_name = userform.cleaned_data.get('name'),
            email = userform.cleaned_data.get('email'),
            point = 0,
            phone = userform.cleaned_data.get('phone'),
            city = userform.cleaned_data.get('city'),
            gu = userform.cleaned_data.get('gu'),
            zipcode = userform.cleaned_data.get('zipcode')
            )
            new_user.save()
            joinform.save()
            return redirect('login')
    else:
        form = JoinForm()
        userform = UserForm()
    return render(request, 'page/join.html', {'form': form, 'userform':userform})

def login(request):
    return render(request, 'page/login.html')

def logout(request):
    return render(request, 'page/main.html')

def cart(request):
    if not request.user:
        results = ""
        return render(request, 'page/cart.html')
    else:
        print(request.user)
    results = Cart.objects.filter(user_id=request.user.username)
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
    if not request.user:
        return redirect('detail', product_id)
    product = Product.objects.get(product_id=product_id)
    try:
        cart_item = Cart.objects.get(user_id=request.user.username, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except Cart.DoesNotExist:
        cartuser = User.objects.get(user_id=request.user.username)
        cart_item = Cart.objects.create(
            user=cartuser,
            product = product,
            quantity = 1
        )
        cart_item.save()
    return redirect('detail', product_id)


def cart_remove(request, product_id):
    if not request.user:
        return redirect('detail', product_id)
    product = get_object_or_404(Product, product_id=product_id)
    cartdelete = Cart.objects.get(user_id=request.user.username, product=product)
    cartdelete.delete()

    return redirect('cart')

def cart_buy(request):
    results = Cart.objects.filter(user_id=request.user.id)
    for result in results:
        result.delete()

    return redirect('cart')

def mypage(request):
    userID = request.user.id
    return render(request, 'page/mypage.html')

def like(request):
    userID = request.user.id
    if not userID:
        results = ""
        return render(request, 'page/like.html')
    results = Likes.objects.filter(user_id=request.user.username)
    context = {
        'products' : results
    }
    return render(request, 'page/like.html', context)


def like_add(request, product_id):
    userID = request.user.id
    if not userID:
        return redirect('detail', product_id)
    product = Product.objects.get(product_id=product_id)
    try:
        like_item = Likes.objects.get(user_id=request.user.username, product=product)
        like_item.save()
    except Likes.DoesNotExist:
        likeuser = User.objects.get(user_id=request.user.username)
        like_item = Likes.objects.create(
            user=likeuser,
            product= product
        )
        like_item.save()

    return redirect('detail', product_id)


def like_remove(request, product_id):
    userID = request.user.id
    if not userID:
        return redirect('detail', product_id)
    product = get_object_or_404(Product, product_id=product_id)
    likedelete = Likes.objects.get(user_id=request.user.username, product=product)
    likedelete.delete()

    return redirect('detail', product_id)

def howto(request):
    return render(request, 'page/howto.html')

def new(request):
    results = Product.objects.filter(detail_category__icontains="new")
    context = {
        'products' : results
    }
    return render(request, 'page/shop/shopnew.html', context)

def best(request):
    results = Product.objects.filter(detail_category__icontains="best")
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
    product = Product.objects.get(product_id=product_id)
    liked = 0
    if request.user.is_authenticated:
        try:
            like_item = Likes.objects.get(user_id=request.user.username, product_id=product_id)
            liked = 1
        except Likes.DoesNotExist:
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
