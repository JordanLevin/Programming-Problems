class Solution(object):
    def findLUSlength(self, a, b):
        if a==b:
            return -1
        if len(a) == 0:
            return len(b)
        if len(b) == 0:
            return len(a)
        if not a==b:
            return max(len(a), len(b))


