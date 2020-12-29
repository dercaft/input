import sys
from PinyinToText import Pinyin2Text
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication,QPushButton,
                             QLayout,QGridLayout)
from PyQt5 import QtCore
from PyQt5.QtCore import *
import global_var

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.buff_text=[]
        self.select_str=""

        self.SHADOW_WIDITH=0

        self.show_text = QLabel(self)
        self.middle=QLabel(self)
        self.pages=QLabel(self)
        self.qle = QLineEdit(self)
        self.show_result=QLineEdit(self)
        self.copy=QPushButton("Copy")
        self.incp=QPushButton("Nex")
        self.decp=QPushButton("Pre")

        layout=QGridLayout()
        layout.addWidget(self.qle,0,0)

        layout.addWidget(self.pages,0,1)
        layout.addWidget(self.incp, 1, 1)
        layout.addWidget(self.decp, 1, 2)
        layout.addWidget(self.show_text,1,0)
        layout.addWidget(self.middle,2,0)
        layout.addWidget(self.show_result,3,0)
        layout.addWidget(self.copy,3,1)
        self.setLayout(layout)

        self.qle.textChanged[str].connect(self.onChanged)
        self.incp.clicked.connect(self.incPage)
        self.decp.clicked.connect(self.decPage)
        self.copy.clicked.connect(self.copyText)

        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('QLineEdit')
        self.show()

        self.results=[]
        self.results_s=[]
        self.maxp=0
        self.nowp=0
        self.a_num=3
        self.b_num=2
    def onChanged(self, text):
        group = []
        show_str=""
        if len(text):
            while len(text) > 0:
                word, text = global_var.trie.search_part(text)
                group.append(word)

            results0 = Pinyin2Text(group,-1)
            results1 = Pinyin2Text(group,-1,1)
            results1 =list(set(results1).difference(set(results0)))

            self.results=self.merge_list(results0,results1)
            self.maxp=int(len(self.results)/(self.a_num+self.b_num))
        else:
            self.results=[]
            self.maxp=0
        self.updateGUI()

    def keyPressEvent(self, event):
        print("按下：" + str(event.key()))
        string=""
        if (event.key()==Qt.Key_Return):
            self.qle.clearFocus()

        flag=event.key() - Qt.Key_0
        if flag in range(1,10) and len(self.results_s)> flag-1:
            string=self.results_s[flag-1]
        elif len(self.results_s)>0 and event.key()==Qt.Key_Space:
            string=self.results_s[0]
            pass

        if (event.key()==Qt.Key_Plus)or event.key()==Qt.Key_Equal:
            print("++")
            jump=self.a_num + self.b_num
            self.nowp=self.nowp+1 if self.nowp+1<self.maxp else self.maxp

        if (event.key()==Qt.Key_Minus):
            print("--")
            jump=self.a_num + self.b_num
            self.nowp=self.nowp -1 if self.nowp -1>0 else 0

        self.updateGUI()
        self.show_result.setText(string)
        self.select_str=string
        print(self.results_s)
        pass
    def updateGUI(self):
        self.results_s =self.cons_buff()
        show_str=self.cons_show_str()
        self.pages.setText(str(self.nowp)+"/"+str(self.maxp))
        self.adjustSize()
        self.show_text.setText(show_str)
        self.show_text.adjustSize()
        pass
    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.select_str)

    def incPage(self):
        self.nowp = self.nowp + 1 if self.nowp + 1 < self.maxp else self.maxp
        self.updateGUI()
        pass
    def decPage(self):
        self.nowp = self.nowp - 1 if self.nowp - 1 > 0 else 0
        self.updateGUI()
        pass

    def cons_show_str(self):
        if len(self.results_s)<1:
            return ""
        show_str = list(map(lambda x: ' ' + str(x + 1) + '.' + self.results_s[x], range(len(self.results_s))))
        show_str = "".join(show_str)
        return show_str

    def cons_buff(self):
        point=self.nowp*(self.a_num+self.b_num)
        end=point+self.a_num+self.b_num
        if end >=len(self.results):
            end=len(self.results)-1
        return self.results[point:end]

    def merge_list(self,list_a:list,list_b:list):
        merge_list=[]
        i0 = 0
        i1 = 0
        lena=len(list_a)
        lenb=len(list_b)
        while i0 < lena and i1 < lenb:
            for i in range(self.a_num):
                if i0>=lena:break
                merge_list.append(list_a[i0])
                i0+=1

            for i in range(self.b_num):
                if i1>=lenb:break
                merge_list.append(list_b[i1])
                i1+=1
            pass
        if i0 < lena:
            merge_list.extend(list_a[i0:])
            pass
        if i1 < lenb:
            merge_list.extend(list_b[i1:])
            pass
        return merge_list

if __name__ == '__main__':
    global_var.init()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
