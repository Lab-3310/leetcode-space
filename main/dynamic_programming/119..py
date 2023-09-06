"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

https://leetcode.com/problems/pascals-triangle/
 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""



'''
Note from Hottari

Sol. I  (https://www.youtube.com/watch?v=9XQ0SCx03zY)
( A new row is "[ the sum of neighboring elements from '[0] + row[-1] + [0]' ]" )
( calculated from 2nd element )
ex
[1, 1]    -> [0, 1, 1, 0]    -> [0+1, 1+1, 1+0]      -> [1, 2, 1]
[1, 2, 1] -> [0, 1, 2, 1, 0] -> [0+1, 1+2, 2+1, 1+0] -> [1, 3, 3, 1]

Step 1: extend row[i-1] to [0, ..., 0] -> temp = [0] + tri_li[-1] + [0]
Step 2: calculate the sum of neighboring elements.


Sol. II  (https://www.youtube.com/watch?v=nPVEaB3AjUM)
( A new row is " [1] + [ the sum of neighboring elements from row[-1] from 2nd position ] + [1]" )
( calculated from 2nd element )
ex
[1, 2, 1] -> [1] + [1+2, 2+1] + [1] -> [1, 3, 3, 1] 

Step 1: Calculate the sum of neighboring elements 
Step 2: extend row[i] to [1, ..., 1]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        # I
        tri_li = [[1]]
        for i in range(2, numRows+1):
            temp = [0] + tri_li[-1] + [0]
            layer = []
            for j in range(i):
                layer.append(temp[j] + temp[j+1])
            tri_li.append(layer)
        return tri_li
        
        # II
        tri_li = [[1], [1,1]]
        for i in range(2, numRows):
            layer = [1]
            for j in range(2, i+1):
                layer.append(tri_li[i-1][j-2] + tri_li[i-1][j-1])
            tri_li.append(layer + [1])

        return tri_li[:max(numRows, 1)]
