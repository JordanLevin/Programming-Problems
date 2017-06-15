class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> ret;
        if(nums.size()==1){
            ret.push_back(-1);
            return ret;
        }
        if(nums.size()==0){
            return ret;
        }
        int counter;
        int i;
        int next;
        for(int a = 0;a<nums.size();a++){
            counter = 0;
            i = a;
            next = a+1;
            while(true){
                if(next == nums.size())
                    next = 0;
                if(i == nums.size())
                    i = 0;
                if(counter > nums.size()){
                    ret.push_back(-1);
                    break;
                }
                if(nums[next] > nums[i]){
                    ret.push_back(nums[next]);
                    break;
                }
                next++;
                counter++;

                
            }
        }
        return ret;
    }
};