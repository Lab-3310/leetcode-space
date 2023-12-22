"""
https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12



note from Hottari


from S to T
 - - - - - -
|S| | |
 - - - 
| | | |
 - - - 
| | |T|
 - - - 

->
 - - - 
|1|3|1|
 - - - 
|1|5|1|
 - - - 
|4|2|1|
 - - - 

->          calculate bottom row  4, 2, 1 -> 7(1+2+4), 3(1+2), 1
 - - - 
|1|3|1|
 - - - 
|1|5|1|
 - - - 
|7|3|1|     
 - - - 

->          rightmost column ( grid[][n-1] ) must += row+1  
 - - - 
|1|3|3|
 - - - 
|1|5|2|     1, 5, 1 -> 1, 5, 2(1+1)  ==>  1, 3, 1 -> 1, 3, 3(1+1+1)
 - - - 
|7|3|1|     
 - - -      

->          others are min(down, right) -> grid[i][j] = min( grid[i+1][j], grid[i][j+1] )
 -- -- -- 
| 7| 6| 3|  3 -> 6( 3 + min(7, 3)), 1 -> 7( 1 + min(8, 6))
 -- -- -- 
| 8| 7| 2|  5-> 7( 5 + min(3, 2) ),  1 -> 8( 1 + min(7, 7))
 -- -- -- 
| 7| 3| 1|
 -- -- -- 



"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for j in reversed(range(n-1)):
            grid[m-1][j] += grid[m-1][j+1]  # bottom row

        for i in reversed(range(m-1)):
            grid[i][n-1] += grid[i+1][n-1]  # rightmost column
            for j in reversed(range(n-1)):
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        
        return grid[0][0]
