class Solution:
    def removeNthFromEnd(self, head, n):
        count= 0
        fast = current = head
        while current is not None:
            count = count+1
            current= current.next
        reach = count - n 
        if n == count:
            return head.next
        for _ in range(reach-1):
            fast = fast.next
        fast.next = fast.next.next
        return head





       