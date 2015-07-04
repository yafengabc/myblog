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
    os.system("git add .")
    os.system('git commit -m "update"')
    os.system("git pull")
    print("::use hexo g to gen the blog")
    os.system("hexo g")
    print("::update blog")
    os.chdir("public")
    os.system("git pull")
    os.system("git add .")
    os.system("git add --all")
    os.system('git commit -m "auto gen"')
    os.system("git push")
    os.chdir("../")

    pass


run(host="0.0.0.0",port=8081)
