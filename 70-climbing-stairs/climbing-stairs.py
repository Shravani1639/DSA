class Solution(object):
    def climbStairs(self, n):
        seen = {}
        seen[1] = 1
        seen[2] =2
        def climb(n):
            if n in seen:
                return seen[n]
            else:
                seen[n]=climb(n-1)+climb(n-2)
                return seen[n]
        return climb(n)
        