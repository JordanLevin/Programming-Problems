# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    data = []
    minimum = -1
    def getMinimumDifference(self, root):
        del self.data[:]
        self.minimum = -1
        self.traverse(root)
        print(self.data)
        for i in range(len(self.data)-1):
            if self.minimum == -1:
                self.minimum = abs(self.data[i] - self.data[i+1])
            if abs(self.data[i] - self.data[i+1]) < self.minimum:
                self.minimum = abs(self.data[i] - self.data[i+1])
        return self.minimum
    def traverse(self, current):
        if current != None:
            self.traverse(current.left)
            self.data.append(current.val)
            self.traverse(current.right)