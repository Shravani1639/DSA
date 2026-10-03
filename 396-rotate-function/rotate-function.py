class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        totalSum = 0
        for i in range(n):
            totalSum += nums[i]

        currentResult = 0
        for i in range(n):
            currentResult += (nums[i] * i)

        maxResult = currentResult

        for i in range(n - 1, 0, -1):
            valueToBeAdded = totalSum - nums[i]
            currentResult += valueToBeAdded

            valueToBeSubtracted = (nums[i] * (n - 1))
            currentResult -= valueToBeSubtracted

            maxResult = max(maxResult, currentResult)

        return maxResult