from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# 登录
from app.models import Grade, Student, MyUser, Promission
from utils.functions import is_login, get_ticket


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
    #     ticket = request.COOKIES.get('ticket')
    #     if ticket:
    #         user = MyUser.objects.filter(ticket=ticket)
    #         if user:
    #             return render(request, 'index.html')
    #         else:
    #             return HttpResponseRedirect(reverse('app:my_login'))
    #     else:


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
        num = request.GET.get('page_num', 1)
        # 添加班级后返回grade  需要显示所有的班级信息
        grades = Grade.objects.all()
        paginator = Paginator(grades, 2)
        page = paginator.page(num)
        return render(request, 'grade.html', {'grades': page})
        # return render(request, 'grade.html', {'grades': grades,{'page:page'},)


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
        return render(request, 'addstu.html', {'grades': grades})

    if request.method == 'POST':
        # 从post请求中获取s_name
        s_name = request.POST.get('s_name')
        # 获取班级信息
        g_id = request.POST.get('g_id')
        # 性别
        s_sex = request.POST.get('s_sex')
        img = request.FILES.get('s_img')
        # 建立班级实例  并且id 一致 应对学生ID
        grade = Grade.objects.filter(id=g_id).first()
        # 创建学生信息
        Student.objects.create(s_name=s_name,
                               g=grade,
                               img=img,
                               s_sex=s_sex)
        g = Grade.objects.filter(id=g_id).first()
        return HttpResponseRedirect(reverse('app:student'), {'g': g})


# 删除学生
def delstu(request):
    if request.method == 'GET':
        # 获取参数
        s_id = request.GET.get('s_id')
        Student.objects.filter(id=s_id).delete()
        return HttpResponseRedirect(reverse('app:student'))


# 编辑班级
def editgrade(request):
    if request.method == 'GET':
        g_id = request.GET.get('grade_id')
        return render(request, 'addgrade.html', {'grade_id': g_id})

    if request.method == 'POST':
        grade_name = request.POST.get('grade_name')
        g_id = request.POST.get('grade_id')
        g = Grade.objects.filter(id=g_id).first()
        g.g_name = grade_name
        g.save()

        return HttpResponseRedirect(reverse('app:grade'))


# 自写中间件
# 需创建模型
def my_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        password = make_password(password)
        MyUser.objects.create(username=username,
                              password=password)

        return HttpResponseRedirect(reverse('app:my_login'))


def my_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 先验证用户是否存在
        if MyUser.objects.filter(username=username).exists():
            user = MyUser.objects.get(username=username)
            if check_password(password, user.password):
                # 在客户端cookie中保存一个session id值
                res = HttpResponseRedirect(reverse('app:index'))
                ticket = get_ticket()
                res.set_cookie('ticket', ticket)
                # 在服务端保存一个session 值
                user.ticket = ticket
                user.save()

                return res

            else:
                return HttpResponseRedirect(reverse('app:my_login'))
        else:
            return HttpResponseRedirect(reverse('app:my_login'))


def my_logout(request):
    if request.method == 'GET':
        response = HttpResponseRedirect(reverse('app:my_login'))
        response.delete_cookie('ticket')
        return response


def test(request):
    if request.method == 'GET':
        # 查询用户id =1 有哪些权限

        user = MyUser.objects.get(id=1)
        user_promisstion = [i.p_name for i in user.r.r_p.all()]

        # 查询有班级列表权限的用户
        p = Promission.objects.get(p_name='GRADELIST')
