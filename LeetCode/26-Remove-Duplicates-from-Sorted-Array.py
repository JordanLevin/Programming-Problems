class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums)-1:
            if nums[i+1] == nums[i]:
                del nums[i+1]
            else:
                i+=1
        """
        :type nums: List[int]
        :rtype: int
        """
        