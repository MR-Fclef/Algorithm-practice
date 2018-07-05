class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        sign = 1 if x > 0 else -1
        if x<(-1*(2**31)) or x>((2**31-1)):
            return 0
        else:   
            x = abs(x)
            while x > 0:
                answer = answer * 10 + x % 10
                x /= 10
                x = int(x)
            if (sign*answer)<(-1*(2**31)) or (sign*answer)>((2**31-1)):
                return 0
            else:
                return sign*answer

test = Solution()
print(test.reverse(123000))