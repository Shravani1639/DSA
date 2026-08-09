# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        p = dummy  = ListNode(0)
        dummy.next = head
        for _ in range(m-1):
            p = p.next
        cur = p.next
        pre = None 
        for _ in range(n-m+1):
            cur.next,pre,cur = pre,cur,cur.next
        p.next.next = cur
        p.next = pre
        return dummy.next

        