title: oray-update-script
date: 2015-07-05 20:12:51
tags: openwrt linux 花生壳
categories: linux
---
更新花生壳域名脚本：

```bash
#!/bin/sh -
USER="yourname"
PASS="123456678"
DOMAIN="yafengabc.vicp.net"

URL="http://${USER}:${PASS}@ddns.oray.com:80/ph/update?hostname=${DOMAIN}"

if [ -f /tmp/ddns ]; then
    ipstr=`curl http://ddns.oray.com/checkip`
    current_ip=`echo $ipstr|grep -o '[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*'`
    req=`cat /tmp/ddns| grep "${current_ip}"`
    if [ ! -z "${req}" ]; then
        old_ip=`echo ${req}| awk '{ print $2}'`
        if [ "${old_ip}" = "${current_ip}" ]; then
            exit
        fi
    fi
fi
wget -q -O /tmp/ddns -q ${URL}


```


---
Writed by Yafeng
