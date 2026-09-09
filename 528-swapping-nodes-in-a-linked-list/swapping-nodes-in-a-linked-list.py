class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(k-1):
            fast = fast.next
        
        first = fast 
        tail = fast
        while tail.next:
            slow = slow.next
            tail = tail.next
        first.val,slow.val = slow.val,first.val
        return head

        