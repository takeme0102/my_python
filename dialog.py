# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:33:33 2018

@author: takumi
"""

#ダイアログを表示するために必要なモジュール
import tkinter.messagebox as mb

#ダイアログを表示
ans = mb.askyesno("質問", "ラーメンは好きですか？")
if ans == True:
    #OKボタンがあるだけのダイアログを表示
    mb.showinfo("同意", "僕も好きです。")
else:
    mb.showinfo("本当？", "まさか、ラーメンが嫌いだなんて！")