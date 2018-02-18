# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:49:05 2018

@author: takumi
"""

import cgi

print("Content-Type: text/html; charaset=utf-8")
print("")

print("<pre>")

form = cgi.FieldStorage()

mode = form.getvalue("mode", default="")
print("mode=", mode)

print("--- all params ---")
for k in form.keys():
    print(k,"=",form.getvalue(k))