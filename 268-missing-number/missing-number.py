class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = {}
        result = len(nums)
        for i in range(result):
            result = result^i
            result = result^nums[i]
        return result

        