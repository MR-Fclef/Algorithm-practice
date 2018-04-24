class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        maxlen = 0
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = -1
        for i in range(len(s)):
            if dict[s[i]] != -1:
                while start <= dict[s[i]]:
                    dict[s[start]] = -1
                    start += 1
            if i - start + 1 > maxlen: maxlen = i - start + 1
            dict[s[i]] = i
        return maxlen

if __name__ == '__main__':
    s = 'pwwkk'
    print(s[0])
    test = Solution()
    print(test.lengthOfLongestSubstring(s))