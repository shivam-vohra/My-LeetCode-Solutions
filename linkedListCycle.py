# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hash = set()
        while head is not None:
            if head in hash:
                return True
            else:
                hash.add(head)
            head = head.next
        return False