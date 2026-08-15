class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k%n
        val = []
        out = []
        for i in range(n-k):
            val.append(nums[i])

        for j in range(n-k,n):
            out.append(nums[j])

        nums[:] = out + val



