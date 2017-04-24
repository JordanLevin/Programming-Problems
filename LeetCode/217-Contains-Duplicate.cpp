class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::map<int, bool> seen;
        for(int i: nums){
            if(seen[i]){
                return true;
            }
            seen[i] = true;
        }
        return false;
    }
};