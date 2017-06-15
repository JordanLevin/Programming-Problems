/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int sumOfLeftLeavesHelper(TreeNode* root, bool isLeft){
        if(root->left == nullptr && root->right == nullptr){
            if(isLeft)
                return root->val;
            return 0;
        }
        if(root->left != nullptr && root->right != nullptr)
            return sumOfLeftLeavesHelper(root->left, true) + sumOfLeftLeavesHelper(root->right, false);
        else if(root->left != nullptr)
            return sumOfLeftLeavesHelper(root->left, true);
        else
            return sumOfLeftLeavesHelper(root->right, false);
    }
    int sumOfLeftLeaves(TreeNode* root) {
        if(root == nullptr)
            return 0;
        return sumOfLeftLeavesHelper(root, false);
    }

};