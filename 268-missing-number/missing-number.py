class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = {num:True for num in nums}
        n = len(nums)
        for i in range(n+1):
            if i not in seen:
                return i
        