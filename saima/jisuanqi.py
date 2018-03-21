#!/usr/bin/env python
#coding=utf-8

def factorize(n):
    i = 2
    flist = []
    while(i*i<=n):
        while(n%i==0):
            flist.append(i)
            n /= i
        i += 1
    if(n!=1):
        flist.append(n)
    return flist

def charlist(flist):
    clist = []
    for i in range(len(flist)):
        for c in str(flist[i]):
            clist.append(int(c))
        if(i<len(flist)-1):
            clist.append("*")
    return clist

def printclist(clist):
    row1 = [" - ","   "," - "," - ","   "," - "," - "," - "," - "," - "," "]
    row2 = ["| |","  |","  |","  |","| |","|  ","|  ","  |","| |","| |"," "]
    row3 = ["   ","   "," - "," - "," - "," - "," - ","   "," - "," - ","*"]
    row4 = ["| |","  |","|  ","  |","  |","  |","| |","  |","| |","  |"," "]
    row5 = [" - ","   "," - "," - ","   "," - "," - ","   "," - "," - "," "]
    chars = [row1,row2,row3,row4,row5]    
    for i in range(5):
        out = []
        for c in clist:
            if(c=="*"):
                out.append(chars[i][10])
            else:
                out.append(chars[i][c])
        print "".join(out)

while True:
    n = int(raw_input())
    flist = factorize(n)
    clist = charlist(flist)
    printclist(clist)