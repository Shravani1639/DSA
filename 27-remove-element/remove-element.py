class Solution(object):
    def removeElement(self, nums, val):
        seen = {}
        k = 0
        for num in nums:
            if num == val:
                continue
            else:
                nums[k]=num
                k = k+1
                seen[num]=True
        return k
        
        