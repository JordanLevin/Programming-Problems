class Solution {
public:
    int integerBreak(int n) {
        if(n==2)
            return 1;
        if(n==3)
            return 2;
        int three_count = n/3;
        int remainder = n-three_count*3;
        if(remainder==0)
            remainder = 1;
        else if(remainder == 1)
            return pow(3, three_count-remainder)*4;
        return pow(3, three_count)*remainder;
    }
};