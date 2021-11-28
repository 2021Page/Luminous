from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .forms import *
from django.contrib.auth.models import User as django_user
from .models import *
from django.core.exceptions import ObjectDoesNotExist
import pymysql
import json

# 물품 구매 관련 관리: cart, cart_buy, like관련 함수 정의
def open_db_info():
    f = open('db.json')
    data = json.load(f)
    print(data)
    return data

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