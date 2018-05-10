class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # numLen, res, Dict = len(nums), set(), {}
        # if numLen < 3: return []
        # nums.sort()
        # for p in range(numLen):
        #     for q in range(p+1, numLen):
        #         if nums[p]+nums[q] not in Dict:
        #             Dict[nums[p]+nums[q]] = [(p,q)]
        #         else:
        #             Dict[nums[p]+nums[q]].append((p,q))
        # for i in range(numLen): 
        #     T = 0-nums[i]
        #     if T in Dict:
        #         for k in Dict[T]:
        #             if k[0] > i: res.add((nums[i],nums[k[0]],nums[k[1]]))
        # return [list(i) for i in res]
        num = nums
        num.sort()
        res = []
        for i in range(len(num)-2):
            if i == 0 or num[i] > num[i-1]:
                left = i + 1; right = len(num) - 1
                while left < right:
                    if num[left] + num[right] == -num[i]:
                        res.append([num[i], num[left], num[right]])
                        left += 1; right -= 1
                        while left < right and num[left] == num[left-1]: left +=1
                        while left < right and num[right] == num[right+1]: right -= 1
                    elif num[left] + num[right] < -num[i]:
                        while left < right:
                            left += 1
                            if num[left] > num[left-1]: break
                    else:
                        while left < right:
                            right -= 1
                            if num[right] < num[right+1]: break
        return res

test = Solution()
print(test.threeSum([-1, 0, 1, 2, -1, -4]))     
