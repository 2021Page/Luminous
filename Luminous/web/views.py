from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .forms import UserForm, SearchForm
from .models import Product

# Create your views here.

def main(request):
    return render(request, 'page/main.html')

def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect(request, 'page/main.html')
    else:
        form = UserForm()
    return render(request, 'page/join.html')

def login(request):
    return render(request, 'page/login.html')

def logout(request):
    return render(request, 'page/main.html')

def cart(request):
    return render(request, 'page/cart.html')

def mypage(request):
    return render(request, 'page/mypage.html')

def result(request):
    search = request.GET.get('searchstr')
    results = Product.objects.filter(title__icontains=search)
    context = {
        'searchstr' : search,
        'products' : results
    }
    return render(request, 'page/result.html', context)

def howto(request):
    return render(request, 'page/howto.html')

def shop(request):
    context = {}
    return render(request, 'page/shop.html')

def event(request):
    return render(request, 'page/event.html')

def faq(request):
    return render(request, 'page/faq.html')

def location(request):
    return render(request, 'page/location.html')

# def post_list(request):
#     #요청이 오면 post_list.html파일을 게시
#     post_list = Post.objects.all() #Post모델의 모든 인스턴스 가져오기
#     context = {
#         'post_list': post_list, #html로 전달될 값
#     }
#     return render(request, 'blog/post_list.html', context) #템플릿 파일로 해당 딕셔너리의 데이터 전달


# def post_detail(request, post_id):
#     post = Post.objects.get(id=post_id) #Post database에서 데이터를 가져옴
#     context = {
#         'post': post,
#     }
#     return render(request, 'blog/post_detail.html', context)


# def post_new(request):
#     if request.method == 'GET':
#         #parameter가 보여지는 요청일 경우 빈 폼을 보여주겠다는 의미
#         form = PostForm()
#     elif request.method == 'POST':
#         form = PostForm(request.POST, request.FILES) #넘어온 데이터를 받아옴
#         if form.is_valid(): #유효한 데이터라면
#             post = form.save() #받은 데이터를 데이터베이스에 저장
#             # title = form.cleaned_data['title']
#             # content = form.cleaned_data['content']
#             # image = form.cleaned_data['image']
#             # post = Post.objects.create(title=title, content=content, image=image)
#             # post = Post.objects.create(**form.cleaned_data)
#             return redirect('post_detail', post_id=post.id)

#     return render(request, 'blog/post_new.html', { 'form': form,}) #context 내장


# def post_edit(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     #post = Post.objects.get(id=post_id)

#     if request.method == 'GET':
#         #데이터가 채워진 폼을 보여주겠다는 의미
#         form = PostForm(instance=post) #instance = 기존 데이터를 갖고와서 보여줌
#     elif request.method == 'POST':
#         form = PostForm(request.POST, instance=post) #넘어온 수정된 데이터를 받아옴
#         if form.is_valid(): #유효한 데이터라면
#             post = form.save() #받은 데이터를 데이터베이스에 저장
#             # title = form.cleaned_data['title']
#             # content = form.cleaned_data['content']
#             # image = form.cleaned_data['image']
#             # post = Post.objects.create(title=title, content=content, image=image)
#             return redirect('post_detail', post_id=post.id)

#     return render(request, 'blog/post_edit.html', { 'form': form, 'post': post, }) #context 내장

# def post_delete(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     post.delete()
#     return redirect('post_list')