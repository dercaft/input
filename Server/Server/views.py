import os
import sys

from django.http import HttpResponse
from django.shortcuts import render

NULL=" "

def hello(request):
    return HttpResponse("Hello World!")

def input(request):
    context= {}
    request.encoding='utf-8' 
    src="Pinyin"
    pinyin=None
    if(src in request.GET and request.GET[src]):
        context['result']=request.GET["Pinyin"]
        pinyin=request.GET["Pinyin"]
    if(not pinyin):
        return render(request,'input.html')
    # pinyin
    result=["1","2","3"]
    result=["nihao","nali","今天","xianzai","总是"]
    # DL
    neural=["5","6","2","3"]
    output=[]
    for i in range(len(result) if len(result) >len(neural) else len(neural)):
        item=[]
        if(i<len(result)):
            item.append(result[i])
        else:
            item.append(NULL)
        if(i<len(neural)):
            item.append(neural[i])
        else:
            item.append(NULL)
        output.append(item)
    context['result0']=output
    return render(request,'input.html',context)
