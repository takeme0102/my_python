# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:03:03 2018

@author: takumi
"""

# ダイアログを表示するために必要なモジュール
import tkinter.filedialog as fd

#ファイル選択ダイアログを表示する
path = fd.askopenfilename(
        title="処理対象のファイルを指定",
        filetypes=[('HTML','.html')])
print(path)