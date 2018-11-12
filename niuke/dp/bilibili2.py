#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************



def  compareVersionNumber(x,y):
    a  = x.split('.')
    b = y.split('.')
    if int(a[0])>int(b[0]):
        return 1
    elif int(a[0])<int(b[0]):
        return -1
    else:
        if int(a[1])>int(b[1]):
            return 1
        elif int(a[1])<int(b[1]):
            return -1
        else:
            return 0


	


#******************************结束写代码******************************

m = sys.stdin.readline().split(' ')
version1 = m[0]
version2 = m[1]

res = compareVersionNumber(version1,version2)
print(str(res) + "\n")