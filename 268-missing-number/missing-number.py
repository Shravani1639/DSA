class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        for i in range(n):
            sum = sum+nums[i]
        expected = n*(n+1)//2
        return expected - sum


        