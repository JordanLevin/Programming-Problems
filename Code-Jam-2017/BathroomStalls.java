import java.util.*;

public class BathroomStalls{

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int testCases = scan.nextInt();
        for(int i = 0;i<testCases;i++){
            int n = scan.nextInt();
            int k = scan.nextInt();
            boolean[] stalls = new boolean[n+2];
            stalls[0] = true;
            stalls[stalls.length-1] = true;
            for(int q = 0;q<k;q++){
                boolean last = false;
                if(q==k-1)
                    last = true;
                int[] stallMin = new int[n+2];
                int[] stallMax = new int[n+2];
                for(int stall = 1;stall<stalls.length-1;stall++){
                    if(stalls[stall])
                        continue;
                    int left = closestLeft(stall, stalls);
                    int right = closestRight(stall, stalls);

                    stallMin[stall] = Math.min(left, right);
                    stallMax[stall] = Math.max(left, right);

                }
                int max = 0;
                int maxIndex = 0;
                boolean multipleChoices = false;
                for(int j = 0;j<stallMin.length;j++){
                    if(stallMin[j] > max){
                        max = stallMin[j];
                        maxIndex = j;
                        multipleChoices = false;
                    }
                    if(stallMin[j] == max){ //possible issues here with multiple 0 values
                        multipleChoices = true;
                    }
                }
                if(!multipleChoices){
                    if(last)
                        System.out.println("Case #" + i + ": " + stallMax[maxIndex] + " " + stallMin[maxIndex]);
                    stalls[maxIndex] = true;
                    continue;
                }
                max = 0;
                maxIndex = 0;
                multipleChoices = false;
                for(int j = 0;j<stallMax.length;j++){
                    if(stallMax[j] > max){
                        max = stallMax[j];
                        maxIndex = j;
                        multipleChoices = false;
                    }
                    if(stallMax[j] == max){ //possible issues here with multiple 0 values
                        multipleChoices = true;
                    }
                }
                if(!multipleChoices){
                    if(last)
                        System.out.println("Case #" + i + ": " + stallMax[maxIndex] + " " + stallMin[maxIndex]);
                    stalls[maxIndex] = true;
                    continue;
                }
                for(int j = 0;j<stallMax.length;j++){
                    if(stallMax[j]==max){ 
                        if(last)
                            System.out.println("Case #" + i + ": " + stallMax[maxIndex] + " " + stallMin[maxIndex]);
                        stalls[j] = true;
                        break;
                    }
                }

            }
            
        }
    }

    public static int closestLeft(int stallNum, boolean[] stalls){
        int ret = 0;
        for(int i = stallNum;!stalls[i];i--){
            ret++;
        }
        return ret;
    }
    public static int closestRight(int stallNum, boolean[] stalls){
        int ret = 0;
        for(int i = stallNum;!stalls[i];i++){
            ret++;
        }
        return ret;
    }

}
