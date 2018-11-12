#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************


# def  solve(S, T):
#     s_len = len(S)
#     t_len = len(T)
#     arr = []
#     num = 0
#     for i in range(0,s_len-t_len+1):
#         arr.append(S[i:i+t_len])
#     print(arr)
#     for i in range(len(arr)):
#         dic = {} 
#         t = '' 
#         for j in range(t_len):
#             if T[j] not in dic:
#                 dic[T[j]] = arr[i][j]
#         for m in range(t_len):
#             t = t + dic[T[m]]
#         if t == arr[i]:
#             num += 1
#     return num

def  solve(S, T):
    s_len = len(S)
    t_len = len(T)
    num = 0
    # arr = []
    for i in range(0,s_len-t_len+1):
        # if S[i:i+3] in arr:
        #     num += 1
        #     continue
        dic = {} 
        t = '' 
        for j in range(t_len):
            if T[j] not in dic:
                dic[T[j]] = S[i+j]
                t = t + dic[T[j]]
            else:
                t = t + dic[T[j]]
        if t == S[i:i+t_len]:
            # arr.append(t)
            num += 1
    # print(arr)
    return num


#******************************结束写代码******************************


try:
    _S = input()
except:
    _S = None

try:
    _T = input()
except:
    _T = None


res = solve(_S, _T)

print(str(res) + "\n")