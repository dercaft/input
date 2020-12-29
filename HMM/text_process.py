import re
def isHan(text):
    # for python 3.x
    # sample: ishan('一') == True, ishan('我&&你') == False
    # str = re.sub("[A-Za-z0-9\!\%\[\]\,\。\\n\:\,\.]", "", text)
    str=re.sub("[^\u4e00-\u9fff]+","",text)
    return str
def py_split(string):
    group=string.split(" ")
    return group