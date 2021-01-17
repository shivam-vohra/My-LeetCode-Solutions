class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while p1 != None or p2 != None:
            
            if p1 != None:
                x = p1.val
                p1 = p1.next
            else:
                x = 0
            
            if p2 != None:
                y = p2.val
                p2 = p2.next
            else:
                y = 0
                
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            
        if carry > 0:
            curr.next = ListNode(carry)
            
        return dummy.next