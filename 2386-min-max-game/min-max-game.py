class Solution(object):
    def minMaxGame(self, nums):

        while len(nums) > 1:

            n = len(nums)
            result = []

            for i in range(0, n, 2):

                if (i // 2) % 2 == 0:
                    result.append(min(nums[i], nums[i+1]))
                else:
                    result.append(max(nums[i], nums[i+1]))

            nums = result

        return nums[0]
        