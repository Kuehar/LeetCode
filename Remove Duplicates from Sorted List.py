# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        runner = head
        while runner:
            while runner.next and runner.next.val == runner.val:
                runner.next = runner.next.next
            runner = runner.next
        return head
# Runtime: 48 ms, faster than 31.67% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14 MB, less than 21.02% of Python3 online submissions for Remove Duplicates from Sorted List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        origin = head
        pre = head
        head = None if head is None else head.next
        while head:
            if pre.val == head.val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return origin
# Runtime: 44 ms, faster than 58.51% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 13.8 MB, less than 55.82% of Python3 online submissions for Remove Duplicates from Sorted 
