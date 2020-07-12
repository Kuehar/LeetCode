# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        root,dic = head,{}
        while root:
            if root in dic:
                return root
            dic[root] = 1
            root = root.next
        return root
# Runtime: 56 ms, faster than 51.83% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 16.9 MB, less than 51.15% of Python3 online submissions for Linked List Cycle II.
