import sys


inp = sys.stdin.readline().split(' ')
a = inp
print(a)
res = []
arr = {}
for i in range(len(a)):
    if a[i]=='0x0':
        data = []
        start = int(a[i+1][2:])
        style = int(a[i+2][2])
        num = int(a[i+2][3])
        for j in range(num):
            data.append(int(a[i+2+start+j][2:]))
            arr['int(a[i+2+start+j][2:])'] = a[i+2+start+j]  
        data_new = sorted(data)
        print(data_new)
        t = len(arr)
        if style == '0':
            for m in range(len(arr)):
                res.append(arr[str(data[m])])
        else:
            for n in range(len(arr)):
                res.append(arr[str(data[t-n-1])])
print(res)



# print(0x1)
# print(0x25)
# print(0x91)

