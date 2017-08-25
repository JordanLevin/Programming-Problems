class Solution(object):
    def reverse(self, x):
        if '-' in str(x):
            ret = int('-'+str(x)[1:][::-1])
        else:
            ret = int(str(x)[::-1])
        if ret > 2147483647 or ret < -2147483647:
            return 0
        return ret
        """
        :type x: int
        :rtype: int
        """