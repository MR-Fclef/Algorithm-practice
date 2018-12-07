class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d,ans= {},[]
        for i in strs:
            sortstr = ''.join(sorted(i))
            if sortstr in d:
                d[sortstr] += [i]
            else:
                d[sortstr] = [i]
        print(d)
        for i in d:
            tmp = d[i];tmp.sort()
            # print(tmp)
            ans += [tmp]
        return ans
    #     m = []
    #     re = []
    #     for i in range(len(strs)):
    #         tmp = self.strfenge(strs[i])
    #         if tmp not in m:
    #             m.append(tmp)
    #             re.append([])
    #         for index, value in enumerate(m):
    #             if tmp == value:
    #                 re[index].append(strs[i])
    #     print(m)
    #     return re
                
    
    # def strfenge(self,a):
    #     b = []
    #     for i in range(len(a)):
    #         b.append(a[i])
    #     b.sort()
    #     return b

test = Solution()
print(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))