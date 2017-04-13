public class Solution {
    public int hammingDistance(int x, int y) {
        String x1 = String.format("%32s", Integer.toBinaryString(x)).replace(" ", "0");
        String y1 = String.format("%32s", Integer.toBinaryString(y)).replace(" ", "0");
        int answer = 0;
        for(int i = 0;i<x1.length();i++){
            if(x1.charAt(i)!=y1.charAt(i)){
                answer++;
            }
        }
        return answer;
        
        
    }
}