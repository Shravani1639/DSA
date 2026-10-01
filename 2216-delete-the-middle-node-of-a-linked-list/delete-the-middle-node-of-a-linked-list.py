class Solution(object):
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        dummy = ListNode(0)
        dummy.next = head 
        current = dummy
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            current = current.next
        
        current.next = current.next.next
        return head   
        
        
        