# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = []
        while head:
            ans.append(str(head.val))
            head = head.next
        return int(''.join(ans),2)
# Runtime: 16 ms, faster than 99.88% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 13.7 MB, less than 85.59% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
