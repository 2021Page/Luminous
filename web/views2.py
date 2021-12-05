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

# 상품 views: 상품 내용, 디테일, 디테일페이지에서 구매하는 함수 정의
def open_db_info():
    f = open('db.json')
    data = json.load(f)
    print(data)
    return data

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

def detail_buy(request, product_id):
    userID = request.user.username
    dbinfo = open_db_info()
    con = pymysql.connect(host='localhost', user=dbinfo['db_id'], password=dbinfo['db_pw'], db='luminous', charset='utf8')
    curs = con.cursor()
    title = "SELECT title FROM product WHERE product_ID="+str(product_id)
    price = "SELECT price FROM product WHERE product_ID="+str(product_id)
    curs.execute(title)
    data_title = curs.fetchall()
    curs.execute(price)
    data_price = curs.fetchall()

    #현재시간
    time="SELECT DATE_FORMAT(CURDATE(), '%Y-%m-%d')"
    curs.execute(time)
    data_time = curs.fetchall()

    #order_info  테이블에 삽입
    total_price=int(data_price[0][0])+3
    sql= "INSERT into order_info(order_Date, total_Price, order_Status, user_ID) values(%s,%s,%s,%s)"
    curs.execute(sql,(data_time[0][0], str(total_price), 'completed', userID))

    #order_id 불러오기
    sql = "SELECT order_ID from order_info ORDER BY order_ID DESC LIMIT 1"
    curs.execute(sql)
    data_order = curs.fetchall()

    #buy 테이블에 삽입
    sql= "INSERT into buy(order_ID, Product_ID, order_p_name) values(%s,%s,%s)"
    curs.execute(sql,(data_order[0][0], product_id, data_title[0][0]))
    con.commit()
    con.close()
    return redirect('detail', product_id)