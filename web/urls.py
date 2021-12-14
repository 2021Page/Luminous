from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, views2, views3, views4
from .forms import UserForm

urlpatterns = [
    #views
    path('join/', views.join, name='join'),
    path('login/', auth_views.LoginView.as_view(template_name='page/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mypage/', views.mypage, name='mypage'),

    #views2
    path('shop/new/', views2.new, name='new'), 
    path('shop/best/', views2.best, name='best'), 
    path('shop/nail/', views2.nail, name='nail'), 
    path('shop/pedi/', views2.pedi, name='pedi'), 
    path('shop/care/', views2.care, name='care'), 
    path('shop/detail/<int:product_id>/', views2.detail, name='detail'),
    path('shop/detail/<int:product_id>/buy/', views2.detail_buy, name='detail_buy'),

    #views3
    path('', views3.main, name='main'), 
    path('howto/', views3.howto, name='howto'), 
    path('event/', views3.event, name='event'), 
    path('event/participate/', views3.event_pcp, name='event_pcp'),
    path('event/coupon/', views3.event_coupon, name='event_coupon'), 
    path('event/point/', views3.event_point, name='event_point'), 
    path('faq/', views3.faq, name='faq'),
    path('location/', views3.location, name='location'),
    path('result', views3.result, name='result'),
    path('question/', views3.send_contact, name='send'),

    #views4
    path('cart/', views4.cart, name='cart'),
    path('cart/add/<int:product_id>', views4.cart_add, name='cartadd'),
    path('cart/remove/<int:product_id>', views4.cart_remove, name='cartremove'),
    path('cart/buy/', views4.cart_buy, name='buy'),
    path('like/',views4.like, name='like'),
    path('like/add/<int:product_id>', views4.like_add, name='likeadd'),
    path('like/remove/<int:product_id>', views4.like_remove, name='likeremove'),
]