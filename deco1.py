# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:43:56 2018

@author: takumi
"""

def show_func_name(func):
    def wrapper(*args, **kwargs):
        print("--- start: " + func.__name__)
        res = func(*args, **kwargs)
        print("--- end: " + func.__name__)
    return wrapper

@show_func_name
def kakugen1():
    print("賢い者たちの静かな言葉は,　")
    print("愚鈍な人々の叫びよりも聞かれる。　")
    
@show_func_name
def kakugen2():
    print("求め続けなさい。そうすれば与えられます")
    
    
kakugen1()
kakugen2()