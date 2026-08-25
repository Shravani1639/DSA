class Solution(object):
    def pairSum(self, head):
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev 
            prev = slow 
            slow = next_node
        left = head
        right = prev
        max_sum = 0
        while right:
            max_sum = max(max_sum,left.val+right.val)
            left = left.next
            right = right.next
        return max_sum


        