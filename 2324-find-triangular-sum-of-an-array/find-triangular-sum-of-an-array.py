class Solution(object):
    def triangularSum(self, nums):
        i = 0
        result = []
        while len(nums)>1:
            result = []
            for i in range(len(nums)-1):
                sum = (nums[i]+nums[i+1])%10
                result.append(sum)
            nums = result
        return (nums[0])

        