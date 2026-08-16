class Solution(object):
    def getIntersectionNode(self, headA, headB):
        current1 = headA
        current2 = headB
        while current1 != current2:
            current1 = current1.next if current1 else headB
            current2 = current2.next if current2 else headA
        return current1


        

        
         
        