class Solution(object):
    def findDifference(self, nums1, nums2):
        seen1= {}
        seen2= {}
        for num in nums1:
            seen1[num]=True
        for num in nums2:
            seen2[num]=True
        ans1=[]
        ans2=[]
        for num in seen1:
            if num not in seen2:
                ans1.append(num)
        for num in seen2:
            if num not in seen1:
                ans2.append(num)
        return (ans1,ans2)
        