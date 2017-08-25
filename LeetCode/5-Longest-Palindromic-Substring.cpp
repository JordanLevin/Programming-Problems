class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() == 1)
            return s;
        vector<pair<int, int> > palindrome_list;
        //insert all palindromes of size 2 or more into a list
        for(int i = 1;i<s.size();i++){
            if(i+1 < s.size() && s[i-1] == s[i+1]){
                palindrome_list.push_back(pair<int, int>(i, 3));
            }
            if(s[i-1] == s[i]){
                palindrome_list.push_back(pair<int, int>(i, 2));
            }
        }
        //stop if no palindromes were found
        if(palindrome_list.size() == 0)
            return string(1, s[0]);
            
        //for every palindrome found, check if the characters on either side are the same
        //if they are, size can be extended by 2
        bool changes = true;
        while(changes){
            changes = false;
            for(auto& pal: palindrome_list){
                //palindromes with even amount of chars
                if(pal.second%2 == 0 && pal.first + pal.second/2 < s.size() &&
                pal.first - pal.second/2 - 1 >= 0){
                    if(s[pal.first + pal.second/2] == s[pal.first - pal.second/2 - 1]){
                        pal.second +=2;
                        changes = true;
                    }
                }
                //palindromes with odd amounts of chars
                else if(pal.second%2 == 1 && pal.first + (pal.second+1)/2 < s.size() && 
                pal.first - (pal.second+1)/2 >= 0){
                    if(s[pal.first + (pal.second+1)/2] == s[pal.first - (pal.second+1)/2]){
                        pal.second +=2;
                        changes = true;
                    }
                }
            }
        }
        //find the largest palindrome in the list
        pair<int, int> result=*std::max_element(palindrome_list.begin(),palindrome_list.end(),
            [](pair<int, int> a, pair<int, int> b){return a.second < b.second;});
        if(result.second%2 == 0){
            return s.substr(result.first-result.second/2, result.second);
        }
        return s.substr(result.first-(result.second-1)/2, result.second);
        
    }
};