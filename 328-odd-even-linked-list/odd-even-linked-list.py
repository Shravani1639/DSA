class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        fast = head
        slow = head.next
        slow_head = slow
        while slow and slow.next:
            fast.next = fast.next.next
            slow.next = slow.next.next
            fast = fast.next
            slow = slow.next

        fast.next = slow_head
        return head
        