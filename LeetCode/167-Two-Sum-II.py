class Solution(object):
    def twoSum(self, nums, target):
        start = 0
        end = len(nums)-1
        while nums[start] + nums[end] != target:
            if nums[start] + nums[end] > target:
                end -= 1
            else:
                start +=1
        return [start+1, end+1]
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """