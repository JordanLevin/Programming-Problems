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
    int sumNumbers(TreeNode* root) {
        if(root == nullptr){
            return 0;
        }
        if(root->left == nullptr && root->right == nullptr)
            return root->val;
        if(root->left == nullptr){
            root->right->val = stoi(to_string(root->val) + to_string(root->right->val));
            return sumNumbers(root->right);
        }
        if(root->right == nullptr){
            root->left->val = stoi(to_string(root->val) + to_string(root->left->val));
            return sumNumbers(root->left);
        }
        root->right->val = stoi(to_string(root->val) + to_string(root->right->val));
        root->left->val = stoi(to_string(root->val) + to_string(root->left->val));
        return sumNumbers(root->right) + sumNumbers(root->left);
    }
};