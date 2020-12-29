#coding:utf-8
###------
# XMU Cog WuYuhang Project02
# File: text count
# Attention: the Format of input file must be UTF-8
# Important word:
# w2w: Dict 记录各个字之间联系的出现次数 一对一 Value is number
# p2w: Dict 记录每个拼音对应的字 一对多 * 由w2p转换生成 Value is relation
# w2p: Dict 记录每个字对应的拼音 多对一 Value is relation
###------
# Trun it into Functions
import time
import text_process
import pickle
# from global_var import *
import global_var

def process(c1,c2):
    string=c1+c2
    global_var.w2w[string] = global_var.w2w.setdefault(string, 0) + 1

# time_start=time.time()
# for i in range(1000000):
#     # w2w[string] = w2w.setdefault(string, 0) + 1 #较快
# time_end=time.time()
# print('totally cost',time_end-time_start)
def text_train(file_path):
    char1='\0'
    time_start=time.time()
    # Reverse Target FileFolder, get ready for text process

    #Open File
    with open(file_path,'r',encoding='UTF-8') as f:
        train_text=f.readlines()
    # Text process start here
    count=0
    total=len(train_text)
    for i in range(total):
        count+=1
        if count%(int(total/20))==0:
            print(str(count)+'/'+str(total))
        sentence=text_process.isHan(train_text[i])
        for word in sentence:
            # record the time of Pinyin
            if not global_var.w2p.__contains__(word):
                continue
            pinyin=global_var.w2p[word]
            global_var.p_count[pinyin] = global_var.p_count.setdefault(pinyin, 0) + 1
            if char1=='\0':
                char1=word
                global_var.w_count[char1] = global_var.w_count.setdefault(char1, 0) + 1 # record the number of single word such as "的"
                continue
            char2=word
            global_var.w_count[char2] = global_var.w_count.setdefault(char2, 0) + 1 # record the number of single word such as "的"
            process(char1,char2) # record the number of words such as "转换"
            char1=char2
    with open("w2w",'wb') as file: # Save data
        pickle.dump(global_var.w2w,file)
    with open("w_count",'wb') as file:
        pickle.dump(global_var.w_count,file)
    with open("p_count",'wb') as file: # Save data
        pickle.dump(global_var.p_count,file)
    time_end=time.time()
    print('totally cost',time_end-time_start)
    print(file_path+" Finished")

if __name__ == '__main__':
    global_var.init()
    file_path = "pinyin_train.txt"# Trained
    text_train(file_path)