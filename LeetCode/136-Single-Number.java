public class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> seen = new HashMap<Integer, Integer>();
        for(int i: nums){
            if(!seen.containsKey(i)){
                seen.put(i, 1);
            }
            else{
                seen.put(i, seen.get(i)+1);
            }
        }
        for(int i: nums){
            if(seen.get(i) == 1)
                return i;
        }
    return -1;   
    }
}