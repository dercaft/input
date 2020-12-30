import os
import sys

from django.http import HttpResponse
from django.shortcuts import render
from .settings import BASE_DIR
# 添加 HMM 模块路径
sys.path.append(os.path.dirname(BASE_DIR))

from HMM.PinyinToText import API as hmm_api , hmm_init
# 添加 DL 模块路径
# sys.path.append("../../DL")
from DL.dl_api import API as seq_api
NULL=" "
hmm_init()

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
    # hmm
    result=hmm_api(pinyin,is_extend=1)
    # DL
    neural=seq_api(pinyin)
    if(type(neural)==str):
        neural=[neural]
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
