# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:55:16 2018

@author: takumi
"""

#デコレータを多重に重ねる
def wrap_html(func):
    def wrapper(*args, **kwargs):
        s = "<html>"
        s += func(*args, **kwargs)
        s += "</html>"
        return s
    return wrapper

def wrap_body(func):
    def wrapper(*args, **kwargs):
        s = "<body>"
        s += func(*args, *kwargs)
        s += "</body>"
        return s
    return wrapper

@wrap_html
@wrap_body
def show_html(text):
    return text

print(show_html("デコレータのテスト"))