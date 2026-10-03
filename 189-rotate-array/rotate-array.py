class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n 
        def reverse(left, right):
            while left<right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right]=temp
                left = left+1
                right = right-1
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)



        