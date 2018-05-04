class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest = 0
        mindif = 100000
        for i in range(n-2):
            left = i+1
            right = n-1
            while left<right:
                s = nums[i] + nums[left] + nums[right]
                dif = abs(s-target)
                if dif<mindif:
                    mindif = dif
                    closest = s
                if s == target:
                    return closest
                elif s<target:
                    left += 1
                else:
                    right -= 1
        return closest

test = Solution()
print test.threeSumClosest([1,2,4,8,16,32,64,128],82)