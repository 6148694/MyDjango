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
def personalView(request):
    context = {
        "name":"上海-悠悠",
        "n_name":"",
        "age":"20",
        "fancy":["python","django","pytest","ios"],
        "bolg":{
            "url":"http://www.baidu.com",
            "img":"https://img0.baidu.com/it/u=3101694723,748884042&fm=26&fmt=auto&gp=0.jpg"
        }
    }
    class Myblog():
        def __init__(self):
            self.wlname = "王磊"
            self.age = "20"
        def guanzhu(self):
            return 500
        def fensi(self):
            return 1000
    myblog = Myblog()
    context['myblog'] = myblog
    return render(request,"person.html",context=context)
#for 取值
def navlist(request):
    name_list = [
        {
            "type":"科普读物",
            "value":["宇宙知识","百科知识","科学世界","生物世界"]
        },
        {
            "type":"计算机/网络",
            "value":["Java","Python","C语言"]
        },
        {
            "type":"建筑",
            "value":["标准/规范","室内设计","建筑科学","建筑文化"]
        }
    ]
    context = {"name_list":name_list}
    # context = {
    #     "name_list":[]
    # }
    return render(request,"navigationbar.html",context=context)

def block(request):
    return render(request,"block.html")
def chongxie(request):
    return render(request,"chongxie.html")