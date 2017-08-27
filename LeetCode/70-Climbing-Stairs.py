class Solution(object):
    def climbStairs(self, n):
        global seen
        if n in seen:
            return seen[n]
        if n == 2:
            return 2
        if n == 1:
            return 1
        count = self.climbStairs(n-2) + self.climbStairs(n-1)
        seen[n] = count
        return count
        """
        :type n: int
        :rtype: int
        """
seen = {}
