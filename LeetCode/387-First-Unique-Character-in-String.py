class Solution(object):
    def firstUniqChar(self, s):
        seen_before = {}
        for char in s:
            seen_before[char] = 0
        for char in s:
            seen_before[char]+=1
        for i in range(len(s)):
            if seen_before[s[i]] == 1:
                return i
        return -1