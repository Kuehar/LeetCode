# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
# Runtime: 36 ms, faster than 81.57% of Python3 online submissions for Delete Node in a Linked List.
# Memory Usage: 14.7 MB, less than 26.00% of Python3 online submissions for Delete Node in a Linked List.
