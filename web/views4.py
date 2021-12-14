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
    userID = request.user.username
    dbinfo = open_db_info()
    con = pymysql.connect(host='localhost', user=dbinfo['db_id'], password=dbinfo['db_pw'], db='luminous', charset='utf8')
    curs = con.cursor()

    #장바구니에서 Product_ID 가져오기    
    cart_p_ID= "SELECT product_ID, quantity FROM luminous.cart WHERE user_ID='"+userID+"'"
    curs.execute(cart_p_ID)
    product_ID = curs.fetchall()

    #상품이름이랑 가격
    title_list = []
    total_price = 0
    for product in product_ID:
        title = "SELECT title FROM luminous.product WHERE product_ID='"+str(product[0])+"'"
        price = "SELECT price FROM luminous.product WHERE product_ID='"+str(product[0])+"'"
        curs.execute(title)
        data_title = curs.fetchall()
        curs.execute(price)
        data_price = curs.fetchall()
        title_list.append(data_title[0][0])
        total_price += data_price[0][0]*product[1] + 3

    #현재시간
    time="SELECT DATE_FORMAT(CURDATE(), '%Y-%m-%d')"
    curs.execute(time)
    data_time = curs.fetchall()
    # order_info 테이블에 주문한 정보 데이터 삽입
    sql= "INSERT into order_info(order_Date, total_Price, order_Status, user_ID) values(%s,%s,%s,%s)"
    curs.execute(sql,(data_time[0][0], str(total_price), 'completed', userID))
    # order_ID 가져오기
    sql = "SELECT order_ID from order_info ORDER BY order_ID DESC LIMIT 1"
    curs.execute(sql)
    data_order = curs.fetchall()
    print(data_order)

    i = 0
    for product in product_ID:
        # buy테이블에 주문한 상품들 넣기
        sql= "INSERT INTO buy VALUES(%s,%s,%s)"
        curs.execute(sql, (data_order[0][0], product[0], title_list[i]))
        i += 1

    # 장바구니에서 상품 delete 
    sql = "DELETE FROM cart WHERE user_ID='"+request.user.username+"'"
    curs.execute(sql)

    con.commit()
    con.close()

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