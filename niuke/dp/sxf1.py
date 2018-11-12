import sys

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    inp = sys.stdin.readline().split(' ')
    huancun = []
    for i in range(len(inp)):
        huancun.append(int(inp[i]))
    arr.append(huancun)

# print(N)
# print(arr)

def func(x):
    res = []
    huancun = []
    for i in range(len(x)):
        huancun = x[i][0:3]
        if x[i][3]==1:
            print(x[i][0])
            # res.append(x[i][0])
        elif x[i][3]==2:
            print(x[i][1])
            # res.append(x[i][1])
        elif x[i][3]==3:
            print(x[i][2])
            # res.append(x[i][2])
        else:
            for j in range(3,x[i][3]):
                tmp = str(x[i][0])+str(x[i][1])+str(x[i][2])
                while(len(tmp)<=x[i][3]):
                    tmp += str(int(tmp[-1])+int(tmp[-2])+int(tmp[-3]))
            print(tmp[x[i][3]-1])
            # res.append(huancun[2])
    # return res

func(arr)




