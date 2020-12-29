import os.path
import re
import codecs
import time
import TextTrain
import global_var
# Return all files' abs_path under the Root File
def abs_paths(indir):
    infiles = list()  # the absolute path we want
    for root, dirs, files in os.walk(indir):
        for filename in files:
            infiles.append(os.path.join(root, filename))
    return infiles

root_path=global_var.DATASET_PATH
file_list=abs_paths(root_path)
global_var.init()
for file in file_list:
    time_start=time.time()
    # Training
    TextTrain.text_train(file)
    # 
    time_end=time.time()
    print(file,' cost',time_end-time_start,"s")