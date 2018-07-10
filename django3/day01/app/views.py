from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# 登录
from app.models import Grade, Student


def login(requset):
    if requset.method == 'GET':
        return render(requset, 'login.html')

    if requset.method == 'POST':
        username = requset.POST.get('username')
        password = requset.POST.get('password')
        # 验证用户名和密码是否能从数据库中匹配user对象
        # User.objects.filter(username=username,password=password)
        user = auth.authenticate(username=username, password=password)
        if user:
            # 通过验证
            auth.login(requset, user)
            return HttpResponseRedirect(reverse('app:index'))
        else:
            # 验证没通过
            return render(requset, 'login.html')


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        # 第一种
        # return HttpResponseRedirect('/app/login')
        # 第二种

        User.objects.create_user(username=username, password=password)

        return HttpResponseRedirect(reverse('app:login'))


# 注销
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('app:login'))


# 首页
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    if request.method == 'POST':
        pass


# 头部
def head(request):
    if request.method == 'GET':
        return render(request, 'head.html')


# 导航栏
def left(request):
    if request.method == 'GET':
        return render(request, 'left.html')


# 班级
def grade(request):
    if request.method == 'GET':
        # 添加班级后返回grade  需要显示所有的班级信息
        grades = Grade.objects.all()
        return render(request, 'grade.html', {'grades': grades})


# 添加班级
def addgrade(request):
    if request.method == 'GET':
        return render(request, 'addgrade.html')

    if request.method == 'POST':
        # 创建班级信息
        g_name = request.POST.get('grade_name')
        Grade.objects.create(g_name=g_name)
        # g = grade(name=name)  g.save()  一样
        return HttpResponseRedirect(reverse('app:grade'))


# 学生
def student(request):
    if request.method == 'GET':
        stus = Student.objects.all()
        return render(request, 'student.html', {'stus': stus})


# 添加学生
def addstu(request):
    if request.method == 'GET':
        grades = Grade.objects.all()
        return render(request, 'addstu.html',{'grades':grades})

    if request.method == 'POST':
        # 从post请求中获取s_name
        s_name = request.POST.get('s_name')
        # 获取班级信息
        g_id = request.POST.get('g_id')
        #性别
        s_sex = request.POST.get('s_sex')
        # 建立班级实例  并且id 一致 应对学生ID
        grade = Grade.objects.filter(id=g_id).first()
        # 创建学生信息
        Student.objects.create(s_name=s_name,
                               g=grade)
        return HttpResponseRedirect(reverse('app:student'))
