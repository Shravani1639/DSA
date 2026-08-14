# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        stack = []
        slow = fast = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        max_sum = 0
        while slow:
            max_sum = max(max_sum,stack.pop()+slow.val)
            slow = slow.next
        return max_sum
