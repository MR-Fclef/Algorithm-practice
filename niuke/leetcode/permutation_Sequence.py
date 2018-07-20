class Solution:

#方法三：效率相对更高一点
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ''
        fact = [1] * n
        num = [str(i) for i in range(1, 10)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        k -= 1
        for i in range(n, 0, -1):
            first = k // fact[i - 1]
            k %= fact[i - 1]
            ans += num[first]
            num.pop(first)
        return ans

'''
#方法二：南郭的方法，效率比较低
    def getPermutation(self, n, k):
        res = ''
        k -= 1
        fac = 1
        for i in range(1, n): fac *= i
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in reversed(range(n)):
            curr = num[int(k/fac)]
            res += str(curr)
            num.remove(curr)
            if i !=0:
                k %= fac
                fac /= i
        return res
'''
'''
    # 方法一：递归时间超出
    # def getPermutation(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: str
        """
    #     li = [i for i in range(1,n+1)]
    #     print(li)
    #     self.flag = 0
    #     self.d = k
    #     self.gg = True
    #     self.re = ''
    #     self.dfs(li,'')
    #     return self.re 
    # def dfs(self,a,c):
    #     if len(a)==0:
    #         self.flag = self.flag + 1        
    #         if self.flag == self.d:
    #             self.gg = False
    #             self.re = c
    #     if self.gg == True:
    #         for i in range(len(a)):
    #             self.dfs(a[0:i]+a[i+1:],c+str(a[i]))
'''

test = Solution()
print(test.getPermutation(4,9))