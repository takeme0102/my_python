# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:24:44 2018

@author: takumi
"""

from  tkinter import *

#テキストの文字を数える関数
def count_text(event):
    s = main_text.get(1.0, END)
    info_label.config(text="{0}文字".format(len(s)))
    
#メインウィンドウ
root = Tk()
root.title('テキストカウンタ')

main_text = Text(root)
main_text.bind("<Key>", count_text)
main_text.pack()

#文字数を表示するラベルを作成
info_label = Label(root)
info_label.pack()

root.mainloop()