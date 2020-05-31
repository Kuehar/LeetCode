# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tempsum = 0
        root = cur = ListNode(0)
        while l1 or l2 or tempsum:
            if l1: tempsum += l1.val; l1 = l1.next
            if l2: tempsum += l2.val; l2 = l2.next
            cur.next = cur = ListNode(tempsum % 10)
            tempsum //= 10
        return root.next
# Runtime: 64 ms, faster than 95.04% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.9 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
