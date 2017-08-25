class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1:
            return 1
        start = 0
        end = 0
        max = 0
        for i in range(1, len(s)):
            end = i
            if s[end] in s[start:end]:
                if end-start > max:
                    max = end-start
                start += s[start:end].index(s[end])+1
            elif end-start+1 > max:
                max = end-start+1
        return max
        """
        :type s: str
        :rtype: int
        """
        