class Solution(object):
    def arrayNesting(self, nums):
        totalseen = set()
        longest = 0
        for i in nums:
            seen = set()
            chain = []
            n = i
            while n not in seen:
                if n in totalseen:
                    break
                totalseen.add(n)
                chain.append(n)
                n = nums[n]
            if len(chain) > longest:
                longest = len(chain)
        return longest
        """
        :type nums: List[int]
        :rtype: int
        """
        