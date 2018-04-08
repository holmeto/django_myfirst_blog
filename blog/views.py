from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import  Category,Blog,Comment,User
from django.http import HttpResponse,Http404
from blog.form import CommentForm,UserForm,BlogForm
from datetime import datetime




def category_html(request):
    category_list=Category.objects.all()
    return render(request,'Category.html',{'category_list':category_list})


def Tag_html(request):
    Tag_list=Tag.objects.all()
    return render(request,'Tag.html',{'Tag_list':Tag_list})

'''def Blog_html(request):
    Blog_list=Blog.objects.all()
    return render(request,'Blog.html',{'blog_list':Blog_list})
'''
def Comment_html(request):
    Comment_list=Comment.objects.all()
    return render(request,'Comment.html',{'Comment_list':Comment_list})


def get_all_blogs(req):
    username=req.COOKIES.get('username','')
    blogs=Blog.objects.all().order_by('-pub_time')
    return render(req,'blog_list.html', {'blogs': blogs,'username':username,})
def blog_get_detail(request,blog_id):
    try:
        blog=Blog.objects.get(id=blog_id)
    except:
        raise Http404
    info_data = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-pub'),  # comment_set是个什么东东？
    }
    return render(request,'blog_details.html',info_data)

def write_blog(req):
    username = req.COOKIES.get('username', '')
    user_id=User.objects.get(username=username).id
    blogs=Blog.objects.all()
    num=2
    for i in blogs:
        num+=1
    if req.method =='POST':
        data = BlogForm(req.POST)
        if data.is_valid():
            #获得表单数据
            title = data.cleaned_data['title']
            content = data.cleaned_data['content']
            category = data.cleaned_data['category']
            #tag = data.cleaned_data['tag']
            #添加到数据库
            blog=Blog(title= title,content=content,category=Category(category))
            blog.id=num
            pub_time=datetime.now()
            #blog.tag.add(tag)
            blog.user_id=user_id
            blog.pub_time = pub_time
            blog.save()
            return HttpResponseRedirect('/blog/')         #写完重定向至博客首页
    else:
        data = BlogForm()
    return render(req,'write_blog.html',{'data':data},)





def comment_get_detail(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except:
        raise Http404
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data  # 清洗数据，形成字典
            cleaned_data['blog'] = blog  # 加入blog信息
            Comment.objects.create(**cleaned_data)  # 加入Comment对象
            return HttpResponseRedirect('/detail/%s/'%blog_id)
    else:
        form = CommentForm()
    info_data={
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-pub'),    #comment_set是django中对外键的调用
        'form':form,
    }

    return render(request,'comment_submit.html',info_data)

# Create your views here.
def register(req):                                              #注册账户
    if req.method =='POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponseRedirect('/login/')         #注册成功重定向至登陆页面
    else:
        uf = UserForm()
    return render(req,'register.html',{'uf':uf},)

def login(req):                                               #登陆账户
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转blog主页
                response = HttpResponseRedirect('/blog/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                uf = UserForm()
                render(req, 'login.html', {'uf': uf})
    else:
        uf = UserForm()
    return render(req,'login.html',{'uf':uf})



def present_all_blogs(req):
    blogs = Blog.objects.all().order_by('-pub_time')
    return render(req, 'All_Users_blog_list.html', {'blogs': blogs})


'''
def logout(req):
        # response = HttpResponse(‘logout !!‘)
        response = HttpResponseRedirect('/apps/login/')
        response.delete_cookie('sername')
        return response'''