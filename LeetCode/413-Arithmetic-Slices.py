class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        count = 0;
        for i in range(0,len(nums)):
            for j in range(i, len(nums)+1):
                if j-i < 3:
                    continue
                if self.isArithmetic(nums[i:j]):
                    count+=1
                else:
                    break
        return count
    def isArithmetic(self, nums):
        prev = nums[0] - nums[1]
        success = True
        for j in range(1,len(nums)-1):
            if nums[j] - nums[j+1] != prev:
                success = False
                break
        return success