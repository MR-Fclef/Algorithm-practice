# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x:x.start)
        length=len(intervals)
        if length ==0:
            return []
        else:
            res=[intervals[0]]
        for i in range(1,length):
            if intervals[i].start<=res[-1].end:
                res[-1].end = max(intervals[i].end,res[-1].end)
            else:
                res.append(intervals[i])
        return res



