import sys
from collections import Counter
#>>> from collections import Counter
#>>> c = Counter()

# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass

#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass

#     return False

# inp = sys.stdin.readline()
# n = len(inp)
# ite = 0
# arr = []
# while(ite<=n-1):
#     huancun = []
#     tmp = ite
#     for i in range(tmp+1,n):
#         if is_number(inp[tmp:i]):
#             huancun.append(int(inp[tmp:i]))
#             ite = i
#     ite += 1
    
#     if huancun:
#         arr.append(huancun[-1])

# print(arr)


inp = sys.stdin.readline()
n = len(inp)
inp = inp[0:n-1]
inp_low = inp.lower()
# print(inp_low)
dic_low = Counter(inp_low)
dic_new = dict(dic_low)
#print(dic_new)
Max = 0
Str =''
for i in dic_new:
    if i.isalpha():
        tmp = dic_new[i.lower()]
        if tmp > Max:
            Max = max(Max,tmp)
            Str = i
print(Str.upper()+str(Max))






# t = sorted(dic_new.items())
# print(t)
# if dic[i]>=dic[i.upper()]:
#     print(i+str(dic_low[i]))
# else:
#     print(i.upper()+str(dic_low[i]))


