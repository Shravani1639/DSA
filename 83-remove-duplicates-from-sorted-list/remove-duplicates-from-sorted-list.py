class Solution(object):
    def deleteDuplicates(self, head):
        seen = {}
        current = head 
        prev = None
        while current:
            if current.val in seen:
                prev.next = current.next
            else:
                seen[current.val] =True
                prev = current
            current = current.next
        return head
