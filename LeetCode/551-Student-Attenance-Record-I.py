class Solution(object):
    def checkRecord(self, s):
        a_count = 0
        for i in s:
            if i == 'A':
                a_count+=1
        if a_count > 1:
            return False
        for i in range(1, len(s)-1):
            if s[i] == 'L' and s[i+1] == 'L' and s[i-1] == 'L':
                return False
        return True