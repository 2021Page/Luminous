from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main, name='main'), 
    #url상에서 page로 진입하면 main이름의 view 함수로 연결해줌
    path('join/', views.join, name='join'),
    path('login/', auth_views.LoginView.as_view(template_name='page/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cart/', views.cart, name='cart'),
    path('mypage/', views.mypage, name='mypage'),
    path('result', views.result, name='result'),

    path('howto/', views.howto, name='howto'), 
    path('shop/', views.shop, name='shop'), 
    path('event/', views.event, name='event'), 
    path('faq/', views.faq, name='faq'),
    path('location/', views.location, name='location'),

    #path('posts/<int:post_id>', views.post_detail, name='post_detail'), 
    #path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
]