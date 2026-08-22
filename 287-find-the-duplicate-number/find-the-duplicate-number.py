class Solution(object):
    def findDuplicate(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                return num
            seen[num] = True 
        return None