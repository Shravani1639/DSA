# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        fast =slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev= None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        first = head
        last = prev
        max_sum = 0
        while last:
            max_sum = max(max_sum,first.val+last.val)
            first = first.next
            last = last.next
            
        return max_sum
