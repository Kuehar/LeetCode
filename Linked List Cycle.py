# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashmap = {}
        while head != None:
            if head in hashmap:
                return True
            hashmap[head] = head
            head = head.next
        return False
# Runtime: 80 ms, faster than 9.62% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        pre,cur = head,head.next
        while pre != cur:
            if not cur or not cur.next:
                return False
            pre,cur = pre.next,cur.next.next
        return True
# Runtime: 84 ms, faster than 8.98% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
