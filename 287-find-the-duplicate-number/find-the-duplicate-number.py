class Solution(object):
    def findDuplicate(self, nums):
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if sum(v <= m for v in nums) - m > 0:
                result = m
                r = m - 1
            else:
                l = m + 1
        
        return result