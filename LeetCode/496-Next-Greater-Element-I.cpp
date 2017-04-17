class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> ret;
        for(int i = 0;i<findNums.size();i++){
            int ret_num = 0;
            bool found_num = false;
            for(int nums_index = 0; nums_index < nums.size(); nums_index++){
                if(found_num){
                    if(nums[nums_index] > findNums[i]){
                        ret_num = nums[nums_index];
                        break;
                    }
                }
                if(nums[nums_index] == findNums[i]) found_num = true;
            }
            if(ret_num == 0) ret_num = -1;
            ret.push_back(ret_num);
        }
        return ret;
    }
};