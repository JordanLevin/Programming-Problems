class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i, k in enumerate(haystack):
            if i+len(needle) > len(haystack):
                return -1
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        