from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render

def hello(request):

    res = {
        "code":0
    }
    return JsonResponse(res)

def login(request):
    # result = {
    #     "year":year,
    #     "month":month
    # }

    return render(request,"login.html",{"year":2021})

def lianxi (request,age,name):
    information = {
        "age":age,
        "name":name
    }
    return JsonResponse(information)
def person(request):
    context = {
        "name":"王磊",
        "n_namer":"磊子",
        "age":30,
        "fancy":["语文","数学","英语","计算机"],
        "bolg":{
            "url":"http://www.baidu.com",
            "img":"https://img0.baidu.com/it/u=3101694723,748884042&fm=26&fmt=auto&gp=0.jpg"
        }
    }
    return render("person.html",context=context)