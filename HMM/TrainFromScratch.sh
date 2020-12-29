#!/usr/bin/env bash
conda activate input
# 先生成最开始的文件
python Data_Init_EarlyStage.py
# # 生成Trie树
# python Trie_init.py
# 遍历数据集进行训练
python Traversal_Files&Train.py
# 开始使用
python PinyinToText.py

