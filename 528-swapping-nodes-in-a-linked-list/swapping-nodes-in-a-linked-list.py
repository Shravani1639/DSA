class Solution(object):
    def swapNodes(self, head, k):
        fast = slow= head
        for _ in range(1,k):
            fast = fast.next
        tail = fast 
        while tail.next:
            slow = slow.next
            tail = tail.next
        fast.val,slow.val = slow.val,fast.val
        return head 


        
        