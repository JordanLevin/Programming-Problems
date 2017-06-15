public class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        for(int row = 0; row < grid.length;row++){
            for(int col = 0;col < grid[0].length;col++){
                if(grid[row][col] == 0) continue;
                if(row-1 < 0 || row-1 >= grid.length || col >= grid[0].length)
                    perimeter++;
                else if(grid[row-1][col] == 0)
                    perimeter++;
                if(row+1 < 0 || row+1 >= grid.length || col >= grid[0].length)
                    perimeter++;
                else if(grid[row+1][col] == 0)
                    perimeter++;
                if(col+1 < 0 || col+1 >= grid[0].length || row >= grid.length)
                    perimeter++;
                else if(grid[row][col+1] == 0)
                    perimeter++;
                if(col-1 < 0 || col-1 >= grid[0].length || row >= grid.length)
                    perimeter++;
                else if(grid[row][col-1] == 0)
                    perimeter++;
            }
        }
        return perimeter;
    }
}