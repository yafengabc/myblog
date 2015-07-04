#!/usr/bin/env python3

from bottle import run,request,post,route
import os

@post('/commit')
def post():
    print("Get some commit from github")
#    data=request.body
#    datas=data.read()
#    print(datas)
    updateblog()
    
    return "Complete"

def updateblog():
    print("::pull the change from github:")
    os.system("git pull")
    print("::use hexo g to gen the blog")
    os.system("hexo g")
    print("update blog")

    pass


run(host="0.0.0.0",port=8081)
