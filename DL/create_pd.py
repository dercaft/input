### 导出模型权重为pd版
##  以准备部署

from __future__ import print_function
from hyperparams import Hyperparams as hp
import tensorflow as tf
import numpy as np
from prepro import *
from data_load import load_vocab, load_test_data, load_test_string
from train import Graph
import codecs
import distance
import os

from tensorflow.python.framework import graph_io
from tensorflow.python.framework.graph_util import convert_variables_to_constants


g = Graph(is_training=False)

# Load vocab
pnyn2idx, idx2pnyn, hanzi2idx, idx2hanzi = load_vocab()

with g.graph.as_default():    
    sv = tf.train.Supervisor()
    with sv.managed_session(config=tf.ConfigProto(allow_soft_placement=True)) as sess:
        # Restore parameters
        print(hp.logdir)

        sv.saver.restore(sess, tf.train.latest_checkpoint(hp.logdir)); print("Restored!")
        
        graph=g.graph
        output_names=["ToInt32"]
        input_graph_def = graph.as_graph_def()
        frozen_graph = convert_variables_to_constants(sess, input_graph_def, output_names)
                
        writer=tf.summary.FileWriter("./log",frozen_graph)
        writer.flush()
        writer.close()
        graph_io.write_graph(frozen_graph, './deploy', 'deploy.pb', as_text=False)        
        # print("Finish")

        