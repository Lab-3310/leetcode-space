"""
https://leetcode.com/problems/minimum-falling-path-sum/description/

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
 

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.



note from Hottari


|2|1|3|
|6|5|4|
|7|8|9|

|6| ->
temp = 2 
temp = min(2, 1) -> 6+1

|5|
temp = 1 
temp = min(1, 2) = 1
temp = min(1, 3) = 1 -> 5+1
.
.
.
|2|1|3|
|7|6|5|
|7|8|9|

->          
| 2| 1| 3|
| 7| 6| 5|
|13|13|14|     

"""


class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])

        for row in range(1, m):
            for col in range(n):
                temp = matrix[row-1][col]
                if col>0: temp = min(matrix[row-1][col-1], temp)
                if col<n-1: temp = min(matrix[row-1][col+1], temp)
                matrix[row][col] += temp
        
        return min(matrix[m-1])
