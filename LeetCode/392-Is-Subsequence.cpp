class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i_s = 0;
        int i_t = 0;
        if(s.size()==0)
            return true;
        while(i_t != t.size()){
            if(s[i_s] == t[i_t]){
                i_s++;
                i_t++;
            }
            else
                i_t++;
            if(i_s == s.size())
                return true;
        }
        return false;
    }
};