import sys

inp = sys.stdin.readline().split(' ')
m = int(sys.stdin.readline())
data = []
for i in inp:
    data.append(int(i))
# print(data)
a= data[0]
b = data[1]
c = data[2]
d = data[3]
# print(m)
fuhao = ['+','-','*','/']
res = []
res.append(a+b+c+d)
res.append(a+b+c-d)
res.append(a+b+c*d)
res.append(a+b+int(c/d))

res.append(a+b-c+d)
res.append(a+b-c-d)
res.append(a+b-c*d)
res.append(a+b-int(c/d))

res.append(a+b*c+d)
res.append(a+b*c-d)
res.append(a+b*c*d)
res.append(a+b*int(c/d))

res.append(a+int(b/c)+d)
res.append(a+int(b/c)-d)
res.append(a+int(b/c)*d)
res.append(a+int(int(b/c)/d))

res.append(a-b+c+d)
res.append(a-b+c-d)
res.append(a-b+c*d)
res.append(a-b+int(c/d))

res.append(a-b-c+d)
res.append(a-b-c-d)
res.append(a-b-c*d)
res.append(a-b-int(c/d))

res.append(a-b*c+d)
res.append(a-b*c-d)
res.append(a-b*c*d)
res.append(a-b*int(c/d))

res.append(a-int(b/c)+d)
res.append(a-int(b/c)-d)
res.append(a-int(b/c)*d)
res.append(a-int(int(b/c)/d))



res.append(a*b+c+d)
res.append(a*b+c-d)
res.append(a*b+c*d)
res.append(a*b+int(c/d))

res.append(a*b-c+d)
res.append(a*b-c-d)
res.append(a*b-c*d)
res.append(a*b-int(c/d))

res.append(a*b*c+d)
res.append(a*b*c-d)
res.append(a*b*c*d)
res.append(a*b*int(c/d))

res.append(a*int(b/c)+d)
res.append(a*int(b/c)-d)
res.append(a*int(b/c)*d)
res.append(a*int(int(b/c)/d))


res.append(int(a/b)+c+d)
res.append(int(a/b)+c-d)
res.append(int(a/b)+c*d)
res.append(int(a/b)+int(c/d))

res.append(int(a/b)-c+d)
res.append(int(a/b)-c-d)
res.append(int(a/b)-c*d)
res.append(int(a/b)-int(c/d))

res.append(int(a/b)*c+d)
res.append(int(a/b)*c-d)
res.append(int(a/b)*c*d)
res.append(int(a/b)*int(c/d))

res.append(int(int(a/b)/c)+d)
res.append(int(int(a/b)/c)-d)
res.append(int(int(a/b)/c)*d)
res.append(int(int(int(a/b)/c)/d))

if m in res:
    print(1)
else:
    print(0)





    