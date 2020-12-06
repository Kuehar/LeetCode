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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        stack = []
        while node:
            stack.append(node.val)
            node = node.next 
        node = head
        
        while node:
            data = stack.pop()
            if data != node.val:
                return False
            node = node.next
        return True
# Runtime: 68 ms, faster than 73.99% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 24.3 MB, less than 22.68% of Python3 online submissions for Palindrome Linked List.
