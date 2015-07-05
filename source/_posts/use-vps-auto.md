title: 用VPS自动生成HEXO博客
date: 2015-07-05 08:05:29
tags: python hexo auto
categories: python
---
hexo是一个不错的静态博客，但是每次都要手动生成有点太麻烦，也不利于手机书写，正好有个不怎么用
的VPS，我写了个小服务，实现了hexo博客的自动生成，提交。

大体说一下思路：  
首先。使用了github的Webhooks功能，让他在push 或者commit时向我的VPS发送一个POST请求
然后，vps的service接收到该请求后，调用git pull命令同步blog的源代码。用hexo g生成新的网站后
再用git push命令同步到yafengabc.github.io

service的代码如下：

```Python


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
    os.system("git pull --no-edit")
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
    os.system("cp -a public /myblog/")
    pass


run(host="0.0.0.0",port=8081)

```


---
Writed by Yafeng
