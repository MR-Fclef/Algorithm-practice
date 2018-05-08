class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        Str = s
        Str = "#" + "#".join(Str) + "#"
        # print(Str)
        mid = 0
        i = 0
        mx = 0
        Id = 0
        p = [0] * len(Str)
        while i<len(Str):
            if mx > i:
                p[i] = min(p[2*Id-i],mx-i)
            else:
                p[i] = 1
 
            while i-p[i] >=0 and i+p[i] < len(Str) and Str[i-p[i]]==Str[i+p[i]]:
                p[i] += 1
 
            if mx < p[i]+i:
                mx = p[i] + i
                Id = i
            i+=1
        len_r = max(p)
        print(p)
        print(Id,mx)
        print(Str)
        print(mid-int((len_r-1)/2))
        print(mid+int((len_r-1)/2))
        if len_r % 2 > 0:
            mid = int((p.index(max(p))-1)/2)
            len_r = max(p)-1
            print(mid,len_r)         
            return s[mid-int(len_r/2)+1:mid+1+int(len_r/2)]
        else:
            mid = int(p.index(max(p))/2)
            len_r = max(p)-1
            print(mid,len_r)           
            return s[(mid-int((len_r-1)/2)):mid+int((len_r-1)/2)+1]


test = Solution()
s = "cdabadabac"
s1 = "cfbbbbd"
print(test.longestPalindrome(s))