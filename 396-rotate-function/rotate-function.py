class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        sum = 0
        product = 0
        for i in range(0,n):
            sum = sum+nums[i]
            product = i*nums[i]+product 

        res = product
        for i in range(1,n):
            product = product + sum - n*nums[-i]
            res = max(res,product)
        return res


                



        