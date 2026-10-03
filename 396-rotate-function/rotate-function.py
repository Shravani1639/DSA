class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)

        total = sum(nums)

        # F(0)
        f = sum(i * nums[i] for i in range(n))

        result = f

        for i in range(n - 1, 0, -1):
            f = f + total - n * nums[i]
            result = max(result, f)

        return result