# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val >= l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
# Runtime: 32 ms, faster than 89.62% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.8 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ans = ListNode(0)
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    ans.next = l1
                    l1 = l1.next
                else:
                    ans.next = l2
                    l2 = l2.next
            elif l1:
                ans.next = l1
                l1 = l1.next
            elif l2:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
        return temp.next

# Runtime: 28 ms, faster than 97.54% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.9 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ans = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
        ans.next = l1 or l2 
        return temp.next
# Runtime: 36 ms, faster than 70.49% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.