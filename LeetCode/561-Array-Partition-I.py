class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        answer = 0
        for i in range(0, len(nums)-1, 2):
            answer += min(nums[i], nums[i+1])
        return answer