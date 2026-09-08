class Solution:

    def removeNthFromEnd(self, head, n):

        dummyNode = ListNode(-1)
        dummyNode.next = head

        fast = dummyNode
        slow = dummyNode

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummyNode.next
        
        