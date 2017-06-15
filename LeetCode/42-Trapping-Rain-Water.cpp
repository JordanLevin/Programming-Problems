class Solution {
public:
    int trap(vector<int>& height) {
        int total = 0;
        int topleft = 0;
        int topright = 0;
        int l = 0;
        int r = height.size()-1;
        while(l<=r){
            if(height[l] <= height[r]){
                if(height[l] >= topleft)
                    topleft = height[l];
                else
                    total+=topleft - height[l];
                l++;
            }
            else{
                if(height[r] >= topright)
                    topright = height[r];
                else
                    total+=topright - height[r];
                r--;              
            }
        }
        return total;
    }
};