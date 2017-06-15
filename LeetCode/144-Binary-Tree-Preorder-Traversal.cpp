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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        return preorderTraversalHelper(root, ret);
    }
    vector<int> preorderTraversalHelper(TreeNode* root, vector<int>& r){
        if(root != nullptr){
            r.push_back(root->val);
            preorderTraversalHelper(root->left, r);
            preorderTraversalHelper(root->right, r);
        }
        return r;
    }
};