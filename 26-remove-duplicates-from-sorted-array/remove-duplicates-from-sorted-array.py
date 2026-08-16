class Solution(object):
    def removeDuplicates(self, nums):
        seen = {}
        k = 0
        for num in nums:
            if num not in seen:
                nums[k] = num
                k = k+1
                seen[num] = True
        return k