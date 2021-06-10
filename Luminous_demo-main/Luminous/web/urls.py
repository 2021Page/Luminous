from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserForm

urlpatterns = [
    path('', views.main, name='main'), 
    #url상에서 page로 진입하면 main이름의 view 함수로 연결해줌
    path('join/', views.join, name='join'),
    path('login/', auth_views.LoginView.as_view(template_name='page/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>', views.cart_add, name='cartadd'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cartremove'),
    path('cart/buy', views.cart_buy, name='buy'),
    path('mypage/', views.mypage, name='mypage'),
    path('likes/',views.like, name='like'),
    path('likes/add/<int:product_id>', views.like_add, name='likeadd'),
    path('likes/remove/<int:product_id>', views.like_remove, name='likeremove'),

    path('howto/', views.howto, name='howto'), 
    path('shop/new/', views.new, name='new'), 
    path('shop/best/', views.best, name='best'), 
    path('shop/nail/', views.nail, name='nail'), 
    path('shop/pedi/', views.pedi, name='pedi'), 
    path('shop/care/', views.care, name='care'), 
    path('shop/detail/<int:product_id>', views.detail, name='detail'),
    path('event/', views.event, name='event'), 
    path('faq/', views.faq, name='faq'),
    path('location/', views.location, name='location'),
    path('result', views.result, name='result'),
]