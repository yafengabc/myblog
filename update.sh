#!/usr/bin/env bash

hexo g

git add .
git commit -m "update"
git push

cd ./public
git add .
git commit -m "udate"
git push
cd ..
