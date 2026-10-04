class Solution(object):
    def isMonotonic(self, nums):
        i = 0
        n = len(nums)
        if nums[0] <= nums[-1]:
            for i in range(1,n):
                if nums[i] < nums[i-1]:
                    return False
        else:
            for i in range(1,n):
                if nums[i] > nums[i-1]:
                    return False
        return True

        