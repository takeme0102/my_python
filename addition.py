# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 16:57:43 2018

@author: takumi
"""

import cgi

print("Content-Type: text/html")
print("")

form = cgi.FieldStorage()

if (not 'v1' in form) or (not 'v2' in form):
    print("""
        <form>
        <input type="text" name="v1"> +
        <input type="text" name="v2">
        <input type="submit" value="計算">
        </form>
    """)
    
else:
    v1 = form.getvalue("v1", "0")
    v2 = form.getvalue("v2", "0")
    try:
        ans = int(v1) + int(v2)
    except:
        ans = 0
    print("<h1>", ans, "</h1>")