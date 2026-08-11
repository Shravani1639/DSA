class Solution:
    def isPalindrome(self, head):
        val = []
        curr = head

        while curr:
            val.append(curr.val)
            curr = curr.next

        return val == val[::-1]
        