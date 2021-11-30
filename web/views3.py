from django.http.response import HttpResponse
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

# 사용자 서비스 관리 views: main, howto, event, faq, location, 서치 결과 관련 함수 정의
def open_db_info():
    f = open('db.json')
    data = json.load(f)
    return data

def main(request):
    news = Product.objects.filter(detail_category__icontains="new")[:3]
    bests = Product.objects.filter(detail_category__icontains="best")[:3]

    context = {
        'news' : news,
        'bests' : bests
    }
    return render(request, 'page/main.html', context)

def howto(request):
    return render(request, 'page/howto.html')

def event(request):
    dbinfo = open_db_info()
    con = pymysql.connect(host='localhost', user=dbinfo['db_id'], password=dbinfo['db_pw'], db='luminous', charset='utf8')
    curs = con.cursor()
    sql = "SELECT * FROM event"
    curs.execute(sql)
    data = curs.fetchall()
    con.close()
    return render(request, 'page/event.html')

def event_coupon(request):
    #쿠폰 개수 올려주는 함수
    dbinfo = open_db_info()
    con = pymysql.connect(host='localhost', user=dbinfo['db_id'], password=dbinfo['db_pw'], db='luminous', charset='utf8')
    curs = con.cursor()
    sql = "SELECT * FROM event"
    curs.execute(sql)
    data = curs.fetchall()
    con.close()
    return render(request, 'page/event.html')

def event_point(request):
    #쿠폰 개수 올려주는 함수
    dbinfo = open_db_info()
    con = pymysql.connect(host='localhost', user=dbinfo['db_id'], password=dbinfo['db_pw'], db='luminous', charset='utf8')
    curs = con.cursor()
    sql = "SELECT * FROM event"
    curs.execute(sql)
    data = curs.fetchall()
    con.close()
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

def send_contact(request):
    userid = request.user.username
    res_num = 0
    if not userid:
        res_num = 2
    else:
        dbinfo = open_db_info()
        con = pymysql.connect(host='localhost', user=dbinfo['db_id'], password=dbinfo['db_pw'], db='luminous', charset='utf8')
        curs = con.cursor()


        sql = "SELECT user_ID, email FROM User WHERE user_ID='"+userid+"'"
        curs.execute(sql)
        data = curs.fetchall()

        comment = request.POST.get('comment', None)
        print("comment: ", comment)
        user_name = ''.join(data[0][0])
        user_email = ''.join(data[0][1])

        sql = "INSERT INTO Questionnaire(email, comment, user_ID) VALUES('"+user_email+"', '"+comment+"', '"+user_name+"')"
        curs.execute(sql)
        con.commit()
        con.close()
        res_num = 1
    
    context = {'res': res_num}
    return HttpResponse(json.dumps(context), content_type="application/json")