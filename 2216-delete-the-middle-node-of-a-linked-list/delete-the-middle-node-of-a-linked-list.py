class Solution(object):
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        fast = slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head
            
        
           
        
        
        