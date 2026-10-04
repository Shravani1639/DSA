class Solution(object):
    def countHillValley(self, nums):
        i = 1 
        j = len(nums)
        hillvalley = 0
        for i in range(1,j-1):
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                i = i+1
                hillvalley = hillvalley+1
            elif nums[i-1]>nums[i] and nums[i]<nums[i+1]:
                i = i+1
                hillvalley = hillvalley+1
            elif nums[i] == nums[i+1]:
                nums[i] = nums[i-1]

        return hillvalley

        