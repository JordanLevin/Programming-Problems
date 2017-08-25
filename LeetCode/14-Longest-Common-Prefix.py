class Solution(object):
    def longestCommonPrefix(self, strs):
        longest = ""
        prev = ""
        #i is character index in string
        if strs==[]:
            return ""
        for i in range(len(strs[0])):
            for j, string in enumerate(strs):
                if i >= len(string):
                    return longest
                if j==0:
                    prev = string[i]
                if string[i] != prev:
                    return longest
                if j == len(strs)-1:
                    longest += string[i]
        return longest
                    
                