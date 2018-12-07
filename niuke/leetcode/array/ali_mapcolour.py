class Solution(object):
    def map_colour(self, n,m):
        if n ==1:
            return m
        elif n ==2:
            if m<2:
                return 0
            else:
                return m*(m-1)
        else:
            if m==2:
                return 2
            elif m<2:
                return 0
            else:
                return m*pow(m-1,n-1)-self.map_colour(n-1,m)
test = Solution()
print(test.map_colour(5,3))