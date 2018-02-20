# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 23:00:16 2018

@author: takumi
"""

import cgi
import cgitb
import os.path
import html

cgitb.enable()

FILE_LOG = "chat-log.txt"

def print_html(body):
    print("Content-type: text/html; charset=UTF-8") 
    print("")
    
    print("""
<html><head><meta charaset="utf-8">
<title>チャット</title></head><body>
<h1>チャット</h1>
<div><form>
名前: <input type="text" name="name" size="8">)
本文: <input type="text" name="body" size="20">
<input type="submit" value="発言">
<input type="hidden" name="mode" value="write">
</form></div><hr>
{0}
</body></html>
    """.format(body))
    
def mode_read(form):
    log = ""
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding='utf-8') as f:
            log = f.read()
    print_html(log)
    
def jump(url):
    print("Status: 301 Moved Permanetly")
    print("Location: " + url)
    print("")
    
    print('<html><head>')
    print('<meta http-equiv="refresh" content="0;'+url+'">')
    print('</head><body>')
    print('<a href="'+url+'">jump</a></body></html>')

def mode_write(form):
    name = form.getvalue("name", "no name")
    body = form.getvalue("body", "")
    
    name = html.escape(name)
    body = html.escape(body)
    with open(FILE_LOG, "a+", encoding='UTF-8') as f:
        f.write("<p>{0}: {1}</p><hr>\n".format(name,body))
    jump('chat.py')
        
def main():
     form = cgi.FieldStorage()
     mode = form.getvalue("mode", "read")
     if mode == "read": mode_read(form)
     elif mode == "write": mode_write(form)
     else: mode_read(form)

if __name__ == "__main__":
    main()