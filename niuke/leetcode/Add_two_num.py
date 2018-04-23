class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:          
            carry = 0
            ret =ListNode(0)
            ret_Last = ret
            
            while(l1 or l2):
                sum = 0
                if(l1):
                    sum = l1.val
                    l1 = l1.next
                if(l2):
                    sum += l2.val
                    l2 = l2.next
                sum += carry
                ret_Last.next = ListNode(sum%10)
                ret_Last = ret_Last.next
                carry = (sum >= 10)
            if(carry):
                ret_Last.next =ListNode(1)
            ret_Last = ret.next
            del ret
            return ret_Last

if __name__ == '__main__':
	l1 = ListNode(2)
	ret1 = l1
	s1 = l1
	l1.next = ListNode(4)
	l1 = l1.next
	l1.next = ListNode(3)
	l1 = l1.next
	lis1 = []
	while(ret1):
		lis1.append(ret1.val)
		ret1 = ret1.next
	print(lis1)
	lis2=[]
	l2 = ListNode(5)
	ret2 = l2
	s2 = l2
	l2.next = ListNode(6)
	l2 = l2.next
	l2.next = ListNode(4)
	l2 = l2.next
	while(ret2):
		lis2.append(ret2.val)
		ret2 = ret2.next
	print(lis2)
	# l2
	test = Solution()
	res = test.addTwoNumbers(s1,s2)
	lis = []
	while(res):
		lis.append(res.val)
		res = res.next
	print(lis)