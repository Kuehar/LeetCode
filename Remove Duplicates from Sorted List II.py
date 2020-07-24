# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        node = pre = ListNode(0)
        node.next = cur = head
        while cur.next:
            nex = cur.next
            if cur.val == nex.val:
                while(nex.next and nex.val == nex.next.val):
                    nex = nex.next
                pre.next = cur = nex.next
                if not cur:
                    return node.next
            else:
                pre,cur,nex = cur,nex,nex.next
        return node.next
# Runtime: 48 ms, faster than 42.22% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 14 MB, less than 18.49% of Python3 online submissions for Remove Duplicates from Sorted List II.
