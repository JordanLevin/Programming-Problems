#include <map>
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::map<int, int> m;
        for(int i: nums){
            if(m.count(i) != 0){
                m[i]++;
            }
            else{
                m[i] = 1;
            }
        }
        
        int maxKey = 0;
        int maxVal = 0;
        for(int i: nums){
            if(m[i] > maxVal){
                maxKey = i;
                maxVal = m[i];
            }
        }
        return maxKey;
    }
};