public class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
        int answer = 0;
        boolean mid = false;
        for(int i=0;i<s.length();i++){
            hm.put(s.charAt(i), hm.getOrDefault(s.charAt(i), 0)+1);
        }
        for(int i: hm.values()){
            if(i%2 == 1 && !mid){
                mid = true;
                answer+=i;
            }
            else if(i%2 == 1){
                answer+=i-1;
            }
            else{
                answer+=i;
            }
        }
        return answer;
    }
}