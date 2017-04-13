public class Solution {
    public int findComplement(int num) {
        String temp = Integer.toString(num, 2);
        String answer = "";
        for(int i = 0;i<temp.length();i++){
            if(temp.charAt(i)=='0')
                answer+='1';
            else
                answer+='0';
        }
        return Integer.parseInt(answer, 2);
    }
}