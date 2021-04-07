# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ans = [head]
        while ans[-1].next:
            ans.append(ans[-1].next)
        return ans[len(ans)//2]
# Runtime: 24 ms, faster than 94.14% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 14.2 MB, less than 73.17% of Python3 online submissions for Middle of the Linked List.
