class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        for n in range(3):
            return n
        a = 1
        b = 2
        i = 3
        while i <= n:
            a, b = b, a + b
            i += 1
        return b
