import pickle
from .GLOBAL import *
from. import Trie
def create_trie():
    obj = Trie.Trie()
    with open(CONFIG_PATH+"p_count", 'rb') as file:
        p_count = pickle.load(file)
    with open(CONFIG_PATH+"potential_w", 'rb') as file:
        potential_w = pickle.load(file)
    tries = list(p_count.keys())
    tries += list(potential_w.keys())
    for key in tries:
        obj.insert(key)
    obj.save()
    print("Trie Created")
    return obj