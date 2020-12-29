from . import global_var
from .text_process import *
import numpy as np
import copy
# import Trie

def possibly_options(last_node, max_prob):
    word_list = []
    word_list.append(last_node)
    # From tail to head, search the chain of max_possibility
    for i in reversed(max_prob):
        kes = i[word_list[-1]]
        word_list.append(kes)
    # Reverse
    word_list.reverse()
    return word_list
def create_trans_matrix(py_group,wordOfPinyin):
    # start S_0
    trans_prob=np.array(list(map(lambda x: global_var.w_count.get(wordOfPinyin[0][x], 1),range(len(wordOfPinyin[0])))))
    trans_prob = trans_prob / np.sum(trans_prob)
    b_=[] # b_i is the Observe Possibility
    trans_Matrix=[]
    length=len(py_group)
    for i in range(len(wordOfPinyin)):
        count=np.ones(len(wordOfPinyin[i]),float)
        it=0
        for j in wordOfPinyin[i]:
            count[it]=global_var.w_count.get(j,1)
            it+=1
        count/=np.sum(count)
        b_.append(count)
    for i in range(length-1):# 对每个拼音和它的下一个
        # 构造两个拼音之间的转移矩阵
        row=len(wordOfPinyin[i])
        col=len(wordOfPinyin[i+1])
        # Create the transmission matrix
        trans_Matrix.append(np.zeros([row,col], dtype = float))
        for l in range(row):
            for k in range(col):
                name=wordOfPinyin[i][l]+wordOfPinyin[i+1][k]
                trans_Matrix[i][l,k]=global_var.w2w.get(name,1)
            trans_Matrix[i][l,...]=trans_Matrix[i][l,...]/sum(trans_Matrix[i][l,...])
    return trans_prob,b_,trans_Matrix

def vertibi( trans_prob,b_,trans_Matrix,res_num=5):
    max_prob = []
    length=trans_Matrix.__len__()
    for i in range(length):
        this_col_max=[]
        this_max_pro=[]
        col=trans_Matrix[i].shape[1]
        for k in range(col): # for every node
            # s_(i+1)=s_i*a_i*b_i
            s_=trans_prob*trans_Matrix[i][...,k]*b_[i]
            this_col_max.append(np.argmax(s_))
            this_max_pro.append(np.max(s_))
        trans_prob=this_max_pro # s_(i+1) emit possibility
        max_prob.append(this_col_max) # record max_node, it is a 2-dimension list
    # Final argmax(s_(n-1)*b_n) is the target number, final number

    s_n=trans_prob*b_[-1]
    # final_word_count=np.argmax(s_n)
    if len(s_n)<res_num or res_num<0: res_num=len(s_n)
    end_lists=np.argsort(-s_n)[:res_num]#Choose max res_num options
    return end_lists,max_prob

def Pinyin2Text(pinyin,res_num=5,is_extend=0):
    wordOfPinyin=[]
    # pinyin group
    py_group= py_split(pinyin) if isinstance(pinyin, str) else copy.deepcopy(pinyin)
    # Create
    tem_py_group=copy.deepcopy(py_group)
    p2w_map=global_var.p2w_extend if is_extend else global_var.p2w

    while len(tem_py_group):
        key=tem_py_group.pop(0)
        if p2w_map.__contains__(key):
            wordOfPinyin.append(p2w_map[key])  # Relavent word of Pinyin
        else:
            py_group.remove(key)
    if len(wordOfPinyin)==0: return []

    # Core Function
    trans_prob,b_,trans_Matrix=create_trans_matrix(py_group,wordOfPinyin)
    end_lists,max_prob=vertibi(trans_prob,b_,trans_Matrix,res_num)
    #Output
    output=[]
    for final_index in end_lists:
        word_list=possibly_options(final_index, max_prob)
        st=list(map(lambda x:wordOfPinyin[x][word_list[x]],range(len(word_list))))
        out_string="".join(list(st))
        output.append(out_string)
    return output
def API(pinyin:str,num:int=5):
    group=[]
    while len(pinyin)>0:
        word,pinyin=global_var.trie.search_part(pinyin)
        group.append(word)
    result=Pinyin2Text(group,num)
    return result
    pass
def hmm_init():
    global_var.init()
if __name__=='__main__':
    global_var.init()
    pinyin=input("Please enter Pinyin:")
    group=[]
    while len(pinyin)>0:
        word,pinyin=global_var.trie.search_part(pinyin)
        group.append(word)
    result=Pinyin2Text(group,3,0)
    print(result)
    result=Pinyin2Text(group,5)
    print(result)

