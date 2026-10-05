class Solution:
    def lastRemaining(self, n):
        left = 1
        right = n
        step = 1
        fromLeft = True

        while left < right:
            nums = (right - left) // step + 1
            if fromLeft:
                left += step
                if nums % 2 == 1:
                    right -= step
            else:
                right -= step
                if nums % 2 == 1:
                    left += step
            fromLeft = not fromLeft
            step *= 2
        return left

