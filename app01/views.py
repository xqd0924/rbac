from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def customers(request):
    if request.method=='POST':
        return HttpResponse('添加成功！')
    return HttpResponse('customers...')

def addcustomer(request):
    return HttpResponse('add customer..')

def editorcustomer(request,id):
    return HttpResponse('editor customer..')

def deletecustomer(request,id):
    return HttpResponse('delete customer..')

def orders(request):

    return HttpResponse('orders...')

def addorders(request):
    return HttpResponse('add order..')

def deleteorders(request,id):
    return HttpResponse('delete order..')

def editororders(request,id):
    return HttpResponse('editor order..')

from app01.models import User
from rbac.service.rbac import initial_session
def login(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
        user=User.objects.filter(name=name,pwd=pwd).first()
        if user:
            request.session['user_id']=user.pk
            initial_session(user,request)
            return redirect('/index/')
    return render(request,'login.html')

import re
def index(request):

    return render(request,'index.html',locals())