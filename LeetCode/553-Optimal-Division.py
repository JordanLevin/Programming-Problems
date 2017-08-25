class Solution(object):
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        return str(nums[0]) + '/(' + str(nums[1:]).replace(', ','/').replace('[','').replace(']','') + ')'
        """
        :type nums: List[int]
        :rtype: str
        """