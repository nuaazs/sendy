from curses.ascii import HT
import imp
from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime
from stores import models
import json
import urllib.parse
# Create your views here.
def index(request):
    return HttpResponse("Hi")

def login(request):
    return render(request,"login.html")

def orm(request):
    # new
    # models.Stores.objects.filter(full_name="不洗脚先生旗舰店").delete()
    models.Stores.objects.create(short_name="b",full_name="不洗脚先生旗舰店",limit=100,remain=50,changed_time=datetime.datetime.now())
    models.Stores.objects.create(short_name="y",full_name="ycy旗舰店",limit=100,remain=50,changed_time=datetime.datetime.now())
    
    data_list = models.Stores.objects.all()
    print(data_list)

    return HttpResponse(data_list)

def get_full_storename(request):
    
    short_name = request.GET.get("short_name")
    print(short_name)
    # full_name = models.Stores.objects.filter(short_name=short_name).first().full_name
    # print(full_name)
    S = models.Stores.objects.filter(short_name=short_name).first()
    # S.full_name = "修改策四"
    # S.save()
    result = {
        "full_name":S.full_name
    }
    ret = json.dumps(result, ensure_ascii=False)

    return HttpResponse(ret)

def change_short_storename(request):
    
    if request.method == 'POST':
        if request.POST:
            print(request.POST)
            full_name = request.POST.get('full_name',0)
            short_name = request.POST.get('short_name',0)
        
            full_name = urllib.parse.unquote(full_name)
            print(full_name)
            S = models.Stores.objects.filter(full_name=full_name).first()
            S.short_name = short_name
            S.save()
            result = {
                "full_name":S.full_name,
                "short_name":S.short_name,
                "status":"success",
            }
            ret = json.dumps(result, ensure_ascii=False)
            return HttpResponse(ret)
        else:
            result = {
                "full_name":"",
                "short_name":"",
                "status":"error",
                "msg":"请求体为空"
            }
            ret = json.dumps(result, ensure_ascii=False)
            return HttpResponse(ret)
    else:
        result = {
                "full_name":"",
                "short_name":"",
                "status":"error",
                "msg":"不支持GET请求"
            }
        ret = json.dumps(result, ensure_ascii=False)
        return HttpResponse(ret)