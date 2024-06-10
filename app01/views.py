from django.shortcuts import render,HttpResponse,redirect
import requests

# Create your views here.
from app01 import models
from app01.models import Department,UserInfo,PrettyNum

def depart_list(request):
    queryset = Department.objects.all()
    return render(request,"depart_list.html",{"queryset":queryset})


def create(request):


    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # UserInfo.objects.create(name="张伟",password="123",age=20,account=30.15,create_time="2022-1-1",depart_id=1,gender=1)
    # UserInfo.objects.create(name="王明",password="456",age=30,account=40.3,create_time="2023-1-1",depart_id=2,gender=1)
    # UserInfo.objects.create(name="李爱",password="789",age=26,account=37,create_time="2024-1-1",depart_id=4,gender=2)
    PrettyNum.objects.create(mobile="12345678912",price=1000,level=1,status=1)
    PrettyNum.objects.create(mobile="12345678913", price=2000, level=2, status=2)
    PrettyNum.objects.create(mobile="12345678914", price=3000, level=3, status=1)


    return HttpResponse("添加成功")

def depart_add(request):
    """ 添加部门 """
    if request.method == "GET":
        return render(request, 'depart_add.html')

    # 获取用户POST提交过来的数据（title输入为空）
    title = request.POST.get("title")

    # 保存到数据库
    Department.objects.create(title=title)

    # 重定向回部门列表
    return redirect("/depart/list/")

def depart_delete(request):
    nid = request.GET.get("nid")
    Department.objects.filter(id = nid).delete()

    return redirect("/depart/list/")

def depart_edit(request,nid):
    if request.method == "GET":
        row_object = Department.objects.filter(id = nid).first()

        return render(request,"depart_edit.html",{"row_object":row_object})

    title = request.POST.get("title")
    Department.objects.filter(id = nid).update(title = title)
    return redirect("/depart/list/")


def user_list(request):
    queryset = UserInfo.objects.all()

    return render(request,"user_list.html",{"queryset":queryset})

def user_add(request):
    if request.method == "GET":
        context={
            "gender_choices" : UserInfo.gender_choices,
            "depart_list" : Department.objects.all()
        }
        return render(request,"user_add.html",context)
    name = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    ac = request.POST.get("ac")
    ctime = request.POST.get("ctime")
    gd = request.POST.get("gd")
    dp = request.POST.get("dp")

    UserInfo.objects.create(name=name,password=pwd,age=age,account=ac,create_time=ctime,depart_id=dp,gender=gd)
    return redirect("/user/list/")

from django import forms

class UserModelForm(forms.ModelForm):
    name = forms.CharField(min_length=2,label="用户名")
    class Meta:
        model = UserInfo #所要添加的models里的类
        fields = ["name","password","age","account","create_time","gender","depart"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # 给每一个输入框的字段，添加class="form-control"
        for name,field in self.fields.items():
            if name == "password":
                continue
            field.widget.attrs = {"class":"form-control","placeholder":field.label}


def user_model_form_add(request):
    if request.method == "GET": #用户打开提交用户的页面时，通过get方法
        form = UserModelForm()
        return render(request,"user_model_form_add.html",{"form":form})

    # 当用户通过POST提交数据，需要对数据校验
    form = UserModelForm(data=request.POST) #生成对象时，继承之前用户填的数据
    if form.is_valid():
        form.save()
        return redirect("/user/list/")

    # 如果校验失败，显示错误信息，再次加载网页
    return render(request,"user_model_form_add.html",{"form":form})

def user_edit(request,nid):
    # 根据ID去获取要编辑的那一行数据对象，
    row_object = UserInfo.objects.filter(id=nid).first()

    # 并把该对象添加到form里，作为编辑的默认值
    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request,'user_edit.html',{'form':form})

    form = UserModelForm(data=request.POST,instance=row_object)
    if form.is_valid():

        # form.instance.password = "987"
        # 在用户手动添加的以外的地方进行提交
        form.save()
        return redirect('/user/list/')
    return render(request,'user_edit.html',{'form':form})

def user_delete(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')

def pretty_list(request):
    queryset = PrettyNum.objects.all()

    return render(request,"pretty_num.html",{"queryset":queryset})

class PrettyNumForm(forms.ModelForm):
    class Meta:
        model = PrettyNum #所要添加的models里的类
        # fields = ["mobile","price","level","status"]
        fields = "__all__"
        # exclude = ['level']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # 给每一个输入框的字段，添加class="form-control"
        for name,field in self.fields.items():
            # if name == "price":
            #     continue
            field.widget.attrs = {"class":"form-control","placeholder":field.label}

def pretty_add(request):
    if request.method == "GET": #用户打开提交用户的页面时，通过get方法
        form = PrettyNumForm()
        return render(request,"pretty_add.html",{"form":form})

    # 当用户通过POST提交数据，需要对数据校验
    form = PrettyNumForm(data=request.POST) #生成对象时，继承之前用户填的数据
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")

    # 如果校验失败，显示错误信息，再次加载网页
    return render(request,"pretty_add.html",{"form":form})


