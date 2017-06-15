#include <algorithm>
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        std::sort(g.begin(), g.end());
        std::sort(s.begin(), s.end());
        int ret = 0;
        for(int i: g){
            for(int j = 0;j<s.size();j++){
                if(s[j]>=i){
                    s.erase(s.begin()+j);
                    ret++;
                    break;
                }
            }
        }
        return ret;
    }
};