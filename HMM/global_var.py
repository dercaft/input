import pickle
from . import Trie_init
from .GLOBAL import *
# CONFIG_PATH="input/HMM/log"

def init():
    global w_count,w2p,w2w,potential_w,p_count,p2w,trie,p2w_extend
    ''''''
    with open(CONFIG_PATH+"w2w",'rb') as file:
        w2w=pickle.load(file) # Numrial, Need to update
    with open(CONFIG_PATH+"w2p",'rb') as file:
        w2p=pickle.load(file) # Relation, Needn't to update
    with open(CONFIG_PATH+"p2w", 'rb') as file:
        p2w = pickle.load(file) # Relation, Needn't to update
    ''''''
    with open(CONFIG_PATH+"w_count", 'rb') as file:
        w_count = pickle.load(file) # Numrial
    ''''''
    with open(CONFIG_PATH+"potential_w",'rb') as file:
        potential_w=pickle.load(file) # Follower of p_count, Need to update
    ''''''
    with open(CONFIG_PATH+"p_count",'rb') as file:
        p_count=pickle.load(file) # Numrial
    trie=Trie_init.create_trie()
    p2w_extend={}
    for key in potential_w:
        if p2w.__contains__(key):
            continue
        for pinyin in p2w:
            if pinyin.startswith(key):
                p2w_extend[key] = p2w_extend.setdefault(key,"")+p2w[pinyin]
    for key in p2w:
        for pi in p2w:
            if key!= pi and pi.startswith(key):
                p2w_extend[key] = p2w_extend.setdefault(key,"")+p2w[pi]

if __name__=='__main__':
    init()
    print(len(w2w))
    print(len(p2w_extend.get('h')))
    print(len(w_count))