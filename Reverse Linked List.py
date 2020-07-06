# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre,cur = None,head
        while cur != None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
# Runtime: 44 ms, faster than 26.15% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.3 MB, less than 67.33% of Python3 online submissions for Reverse Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        stack = []

        while head.next:
            stack.append(head)
            head = head.next

        while stack:
            cur = stack.pop()
            cur.next.next = cur
            cur.next = None

        return head
# Runtime: 40 ms, faster than 46.28% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.1 MB, less than 96.42% of Python3 online submissions for Reverse Linked List.
