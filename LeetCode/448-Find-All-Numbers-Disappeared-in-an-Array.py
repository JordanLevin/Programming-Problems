class Solution(object):
    def findDisappearedNumbers(self, nums):
        ret = []
        numbers = set([i for i in range(1, len(nums)+1)])
        nums = set(nums)
        return list(nums^numbers)