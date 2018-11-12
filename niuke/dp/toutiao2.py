import sys

class Solution:
    def test(self,x,y,z,res):
        if [x[0]+1,x[1]] in y:
            y.remove([x[0]+1,x[1]])
            self.test([x[0]+1,x[1]],y,z,res)
        if [x[0],x[1]+1] in y:
            y.remove([x[0],x[1]+1])
            self.test([x[0],x[1]+1],y,z,res)
        else:
            z = z+1
            if z<len(y):
                # print(z)
                self.test(y[z],y,z,res)
            else:
                res.append(z)
                return
        # print(res)
        return res

        





M = int(sys.stdin.readline())
# print(M)
arr = []

for i in range(M):
    data = []
    data = sys.stdin.readline().split(' ')
    for j in range(M):
        data[j] = int(data[j])
    arr.append(data)
index_1 = []
for i in range(M):
    for j in range(M):
        if arr[i][j]==1:
            index_1.append([i,j])
t = Solution()
res = []
t.test(index_1[0],index_1,0,res)
print(min(res))



