#include <queue>
#include <pair>
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        return search(root);
    }
    
    int search(TreeNode* r){
        std::vector<std::pair<int, TreeNode*> > nodes;
        std::queue<std::pair<int, TreeNode*> > q;
        q.push(std::pair<int, TreeNode*>(0,r));
        while(!q.empty()){
            auto temp = q.front();
            q.pop();
            nodes.push_back(temp);
            if(temp.second->left != nullptr){
                q.push(std::pair<int, TreeNode*>(temp.first+1, temp.second->left));
            }
            if(temp.second->right != nullptr){
                q.push(std::pair<int, TreeNode*>(temp.first+1, temp.second->right));
            }
        }
        if(nodes.size() == 1){
            return nodes[0].second->val;
        }
        for(int i = nodes.size()-1;i>0;i--){
            std::cout << nodes[i].first << " " << nodes[i].second->val << "\n";
            if(nodes[i].first > nodes[i-1].first){
                return nodes[i].second->val;
            }
        }
        return 0;
    }
};