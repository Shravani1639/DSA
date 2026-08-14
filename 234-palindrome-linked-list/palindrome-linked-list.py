class Solution:
    def isPalindrome(self, head):
        val = []
        temp = head 
        while temp is not None:
            val.append(temp.val)
            temp=temp.next

        temp = head
        while temp is not None:
            if temp.val != val[-1]:
                return False

            temp = temp.next 
            val.pop()
        return True
        
        