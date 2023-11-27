"""

https://leetcode.com/problems/unique-paths/


There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 


note from Hottari


from S to T
 - - - - - -
|S| | | | | |
 - - - - - -
| | | | | | |
 - - - - - -
| | | | | |T|
 - - - - - -

(I)
->
 - - - - - -
| | | | | |1|
 - - - - - -
| | | | | |1|
 - - - - - -
|0|0|0|0|0|1|
 - - - - - -

->
 - - - - - -
| | | | | |1|
 - - - - - -
| | | | | |1|
 - - - - - -
|1|1|1|1|1|1|
 - - - - - -

->
 - - - - - -
| | | | | |1|
 - - - - - -
|6|5|4|3|2|1|
 - - - - - -
|1|1|1|1|1|1|
 - - - - - -

->
 -- -- -- -- -- --
|21|15|10| 6| 3| 1|
 -- -- -- -- -- --
| 6| 5| 4| 3| 2| 1|
 -- -- -- -- -- --
| 1| 1| 1| 1| 1| 1|
 -- -- -- -- -- --





(II)
->
 - - - - - -
| | | | | |1|
 - - - - - -
| | | | | |1|
 - - - - - -
|1|1|1|1|1|1|
 - - - - - -

->
 - - - - - -
| | | | | |1|
 - - - - - -
|6|5|4|3|2|1|
 - - - - - -
|1|1|1|1|1|1|
 - - - - - -

->
 -- -- -- -- -- --
|21|15|10| 6| 3| 1|
 -- -- -- -- -- --
| 6| 5| 4| 3| 2| 1|
 -- -- -- -- -- --
| 1| 1| 1| 1| 1| 1|
 -- -- -- -- -- --
 

"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # (I)
        row = [0]*n
        row[n-1] = 1                            # |0|0|0|0|0|1|

        for i in reversed(range(m)):                          
            for j in reversed(range(n-1)):
                row[j] += row[j+1]   

        return row[0]
    

        # (II)
        # row = [1]*n                                     # initial row is bottom row
        # for i in range(m-1):
        #     upper_row = [1]*n                           # initial upper_row (only upper_row[-1] will be used)

        #     for j in range( (n-1)-1, -1, -1):           # bottom and right are all 1
        #         upper_row[j] = upper_row[j+1] + row[j]  # add the right path(upper_row[j+1]) and down path(row[j]) to be a real upper_row
            
        #     row = upper_row                             # update the row                                 
        # return row[0]


