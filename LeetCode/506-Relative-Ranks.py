class Solution(object):
    def findRelativeRanks(self, nums):
        numscopy = nums[:]
        numscopy.sort()
        start = 0
        if len(nums) >=3:
            nums[nums.index(numscopy[len(numscopy)-1])] = "Gold Medal"
            nums[nums.index(numscopy[len(numscopy)-2])] = "Silver Medal"
            nums[nums.index(numscopy[len(numscopy)-3])] = "Bronze Medal"
            start = 4
        elif len(nums) >=2:
            nums[nums.index(numscopy[len(numscopy)-1])] = "Gold Medal"
            nums[nums.index(numscopy[len(numscopy)-2])] = "Silver Medal"
            start = 3
        if len(nums) >=3:
            nums[nums.index(numscopy[len(numscopy)-1])] = "Gold Medal"
            nums[nums.index(numscopy[len(numscopy)-2])] = "Silver Medal"
            nums[nums.index(numscopy[len(numscopy)-3])] = "Bronze Medal"
        for i in range(len(numscopy)-start, -1, -1):
            nums[nums.index(numscopy[i])] = len(numscopy)-i
        return nums
            