class Solution {
public:
    int minMoves(vector<int>& nums) {
        int moves = 0;
        auto min = std::min_element(nums.begin(), nums.end());
        int min_val = *min;
        std::sort(nums.begin(), nums.end());
        while(true){
            if(nums.size() == 0)
                return moves;
            auto max = nums.begin()+nums.size()-1;
            int max_val = *max;
            moves += max_val-min_val;
            nums.erase(max);
        }
    }
};