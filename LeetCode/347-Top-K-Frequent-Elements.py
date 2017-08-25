from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        ret = []
        count = defaultdict(int)
        for i in nums:
            count[i] +=1
        count_sorted = sorted(count.items(), key=lambda x:x[1])
        for i in range(k):
            ret.append(count_sorted[len(count_sorted)-i-1][0])
        return ret
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """