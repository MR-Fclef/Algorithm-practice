# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = {}
        res = head
        #d[head.val] = 1
        while(head):
            if head.val not in d:
                d[head.val] = 1
                pre = head
                head = head.next
            else:
                pre.next = head.next
                head = head.next
            
        return res