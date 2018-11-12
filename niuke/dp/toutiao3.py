import sys



# def dfs(x,loc):
#     x_len = len(x)
#     for i in range(loc,x_len):
#         if int(x[loc:i])<=256 and int(x[loc:i])>=0:
#             dfs(x[i:],i)



# inp = sys.stdin.readline()
# inp = inp[0:len(inp)-1]
# print(inp[0:4])


N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

inp = sys.stdin.readline().split(' ')
data = []
for i in range(len(inp)):
    if i*2 < len(inp):
        data.append([int(inp[i*2]),int(inp[i*2+1])])
print(data)

for i in range(len(data)):
    