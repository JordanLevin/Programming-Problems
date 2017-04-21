class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ret = True;
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, '', 1)
            else:
                ret = False
        return ret