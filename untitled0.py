# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:30:23 2020

@author: LKer
"""
import requests
num = 1
while True:
    url = "http://static.ruiwen.com/img/jiaocai/yuwen/bubianban/yinianjixiace/" + str(num) + ".jpg"
    print(url)
    response = requests.get(url)
    img =response.content
    with open( 'C:/kebeng/{0}.jpg'.format(num),'wb' ) as f:
        f.write(img)
    num = num + 1
    if num > 124:
        break
