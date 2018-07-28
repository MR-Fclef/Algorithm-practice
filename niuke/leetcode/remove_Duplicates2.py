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
        if head is None or head.next is None:
            return head
        
        dummyhead = ListNode(0)
        dummyhead.next = head
        
        p = dummyhead
        while p.next is not None and p.next.next is not None:
            tmp = p
            while tmp.next.val == tmp.next.next.val:
                tmp = tmp.next
                if tmp.next.next is None:
                    break
            if tmp == p:
                p = p.next
            else:
                if tmp.next.next is not None:
                    p.next = tmp.next.next
                else:
                    p.next = tmp.next.next
                    break
        return dummyhead.next