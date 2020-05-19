# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        value = []
        while head:
            value.append(head.val)
            head = head.next
        return value == value[::-1]
# Runtime: 92 ms, faster than 15.28% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 24.1 MB, less than 11.54% of Python3 online submissions for Palindrome Linked List.
