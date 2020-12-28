import os
import sys

from django.http import HttpResponse
from django.shortcuts import render

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
    # DL
    neural="谁啊"
    context['result']=result
    context['neural']=neural
    return render(request,'input.html',context)
