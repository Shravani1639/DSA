class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        out = [0]*n
        for i  in range(n):
            index = (i + nums[i]) % n
            out[i] = nums[index]
        return out


        