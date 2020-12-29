from pd_model import seq2seq
import numpy as np

from hyperparams import Hyperparams as hp
from prepro import *
from data_load import load_vocab, load_test_data, load_test_string

model=seq2seq(model_path='./log/qwerty/deploy.pb')
pnyn2idx, idx2pnyn, hanzi2idx, idx2hanzi = load_vocab()
while True:
    line = input("请输入测试拼音：")
    if len(line) > hp.maxlen:
        print('最长拼音不能超过50')
        continue
    x = load_test_string(pnyn2idx, line)
    #print(x)
    preds = model.inference(x)
    got = "".join(idx2hanzi[idx] for idx in preds[0])[:np.count_nonzero(x[0])].replace("_", "")
    print(got)