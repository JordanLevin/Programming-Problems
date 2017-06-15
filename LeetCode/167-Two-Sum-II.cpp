
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int high = numbers.size()-1;
        int low = 0;
        vector<int> ret;
        while(true){
            if(numbers[high] + numbers[low] < target){
                low++;
            }
            else if (numbers[high] + numbers[low] > target){
                high--;
            }
            else{
                ret.push_back(low+1);
                ret.push_back(high+1);
                return ret;
            }

        }

    }
};
