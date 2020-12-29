from .pd_model import seq2seq
import numpy as np

from .hyperparams import Hyperparams as hp , ROOT_PATH
from .prepro import *
from .data_load import load_vocab, load_test_data, load_test_string

model=seq2seq(model_path=ROOT_PATH+"log/qwerty/deploy.pb")
pnyn2idx, idx2pnyn, hanzi2idx, idx2hanzi = load_vocab()
def API(pinyin:str)->str:
    if len(pinyin) > hp.maxlen:
        print('最长拼音不能超过50')
        return ""
    x = load_test_string(pnyn2idx, pinyin)
    #print(x)
    preds = model.inference(x)
    got = "".join(idx2hanzi[idx] for idx in preds[0])[:np.count_nonzero(x[0])].replace("_", "")   
    return got 