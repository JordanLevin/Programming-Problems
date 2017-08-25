# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if len(nums) == 0:
            return None
        m = max(nums)
        i = nums.index(m)
        x = TreeNode(m)
        x.left = self.constructMaximumBinaryTree(nums[:i])
        x.right = self.constructMaximumBinaryTree(nums[i+1:])
        return x
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        