title: 使用hexo
date: 2015-06-03 10:20:25
tags: 
- linux
- hexo
categories: linux
---
折腾了一下午，终于感觉我的blog处于可用状态了。当然遗留问题还是有的，比如，评论还没来得及搞。
hexo没有想象中的快，我是在树莓派上运行的，生成一次网站要用10秒钟吧，hexo的发布功能即hexo
deployer功能没用成，最后写了一个shell脚本用git提交算了。
最后加了一个hexo new xxx后自动调用vim编辑生成的文件的功能，代码很简单：
把new.js（~/myblog/node_modules/hexo/lib/plugins/console/new.js）最后一句加上：
    spawn("vim",[post.path],{stdio: [process.stdin, process.stdout, process.stderr]});
就可以了，即改成如下的样子：
    return this.post.create(data, args.r || args.replace).then(function(post){
            self.log.info('Created: %s', chalk.magenta(tildify(post.path)));
            
     return this.post.create(data, args.r || args.replace).then(function(post){
            self.log.info('Created: %s', chalk.magenta(tildify(post.path)));
            spawn("vim",[post.path],{stdio: [process.stdin, process.stdout, process.stderr]});
当然，之前别忘了声明一下
	var spawn = require('child_process').spawn

Writed by Yafeng
