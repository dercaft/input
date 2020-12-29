import os
from global_var import *
#INITAILIZE ALL GLOBAL VARIBLES

###------
# XMU Cog WuYuhang Project02
# File: pinyin2word
# Attention: the Format of input file must be UTF-8
# Important word:
# w2w: Dict 记录各个字之间联系的出现次数 一对一 Value is number
# p2w: Dict 记录每个拼音对应的字 一对多 * 由w2p转换生成 Value is relation
# w2p: Dict 记录每个字对应的拼音 多对一 Value is relation
###------
import re
import text_process
import pickle
w2p={} # 键值: 字符串
p2w={} # 键值: 字符串
p_count={}
potential_w={}
w2w={}
w_count={}

lines=[]
with open("pinyin.txt",'r',encoding='utf-8') as f:
    lines=f.readlines()
for line in lines:
    key=re.match("[a-z]+",line).group()
    p2w[key]=text_process.isHan(line)
for pinyin in p2w:
    for word in p2w[pinyin]:
        w2p[word]=pinyin

with open("p2w",'wb') as fp:
    pickle.dump(p2w,fp)
with open("w2p",'wb') as fp:
    pickle.dump(w2p,fp)
#
#init()
#
pinyin_text=lines
with open("pinyin.txt",'r',encoding='UTF-8') as f:
    pinyin_text=f.readlines()
for lens in pinyin_text:
    pinyin=re.match('[\w]+', lens, flags=0).group()
    p_count[pinyin] = p_count.setdefault(pinyin, 0)
    p_count[pinyin]=0
for key in p_count.keys():
    length=len(key)
    if length<2:
        continue
    for i in range(1,length):
        strs=key[0:i]
        if p2w.__contains__(strs):
            continue
        potential_w[strs]=''

with open("potential_w",'wb') as file:
    pickle.dump(potential_w,file)

for cha in p_count:
    p_count[cha]=0
with open("p_count",'wb') as file: # Save data
    pickle.dump(p_count,file)

for cha in w2w:
    w2w[cha] = 0
with open("w2w",'wb') as file: # Save data
    pickle.dump(w2w,file)

for cha in w_count:
    w_count[cha]=0
with open("w_count",'wb') as file:
    pickle.dump(w_count,file)
print("Relatioship Between Pinyin and words established")
