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

# Create your views here.
def open_db_info():
    f = open('db.json')
    data = json.load(f)
    return data

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

def mypage(request):
    userID = request.user.username
    dbinfo = open_db_info()
    con = pymysql.connect(host='localhost', user=dbinfo['db_id'], password=dbinfo['db_pw'], db='luminous', charset='utf8')
    curs = con.cursor()
    sql = "SELECT * FROM luminous.user_mypage WHERE user_ID='"+userID+"'"
    curs.execute(sql)
    data = curs.fetchall()
    sql2 = "SELECT count(*) FROM luminous.coupon WHERE user_ID='"+userID+"'"
    curs.execute(sql2)
    data2 = curs.fetchall()

    #주문내역
    order_p_list = []
    sql3 = "SELECT order_ID, order_Date, total_Price, order_Status FROM luminous.order_info WHERE user_ID='"+userID+"'"
    curs.execute(sql3)
    data3 = curs.fetchall()
    for per_order in data3:
        per_order_p_str = ""
        sql4="SELECT order_p_name FROM buy WHERE order_ID="+str(per_order[0])
        curs.execute(sql4)
        data4 = curs.fetchall()
        i = 0
        for order_product in data4:
            if i == 0:
                per_order_p_str += order_product[0]
                i+=1
            else:
                per_order_p_str = per_order_p_str + ", " + order_product[0]
        order_p_list.append(per_order_p_str)
    
    con.close()

    cur_orderlist = list(data3) #주문내역 튜닝
    orderlist = []
    i = 0
    for order in cur_orderlist:
        order = list(order)
        order.insert(2, order_p_list[i])
        i+=1
        orderlist.append(order)

    context = {
        'user_name':data[0][1], #유저이름
        'point' : data[0][2], #포인트
        'coupon': data2[0][0], #쿠폰
        'order_list': orderlist, #주문내역
    }
    
    return render(request, 'page/mypage.html', context)