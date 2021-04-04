# 在线输入法
## 项目环境

- python 3.6
- django 2.2
- tensorflow 1.15

这里只列出部分重要python包，依赖环境的详细信息请查阅requirement.yaml

#### conda一键安装可运行的虚拟环境
* 注意 *：需要修改requirement文件的-prefix部分，改成你自己的anaconda虚拟环境路径

```
conda create -n <ENV_NAME> -f requirement.yaml
```

## 使用指南

### HMM

#### 从头训练

##### 准备数据集

只要有文本就可以，对于格式没有要求，实测txt和csv均可接受处理并用来训练。

##### 运行自动训练脚本

进入HMM文件夹：

```bash
bash TrainFromScratch.sh
```

#### 使用预训练权重

1. 下载权重 [百度云](https://pan.baidu.com/s/1CVsUH-KmDlE06xgoR8unhQ) 提取码 oecf

2. 移动到hmm文件夹下

### DL - seq2seq

#### 从头训练

1. 下载数据集 [Leipzig Chinese Corpus](http://wortschatz.uni-leipzig.de/en/download/)

2. 构造拼音汉字平行语料库

   ```bash
   python build_corpus.py
   ```

3. 构造vocab表

   ```
   python prepro.py
   ```

4. 训练

   ```
   python train.py
   ```

#### 直接使用

1. 下载预训练pd文件和vocab表文件: [百度云](https://pan.baidu.com/s/1CVsUH-KmDlE06xgoR8unhQ) 提取码 oecf

2. 将预训练权重和vocab表移动到指定位置

   进入DL文件夹：

   ```bash
   # 创建pd权重需要的文件夹
   mkdir log && mkdir log/qwerty 
   mv deploy.pd log/qwerty # 移进去
   # 创建vocab表需要的文件夹
   mkdir data
   mv vocab.qwerty.pkl data
   ```

3. 运行test.py测试模型

   ```
   python test.py
   ```

### 启动服务

进入到Server文件夹下运行：

```
python manage.py runserver 0.0.0.0:8000
```

更多操作请查阅Django资料：

- [官方文档](https://docs.djangoproject.com/zh-hans/2.2/)
- [菜鸟Django教程](https://www.runoob.com/django/django-tutorial.html)

