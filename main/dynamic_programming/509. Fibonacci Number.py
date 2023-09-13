"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""


'''
Note from Hottari


Sol. I

Step 1: initialize the f[0], f[1] -> fib_li = [0, 1]
Step 2: calculate f[n] for f[n] = f[n-2] + f[n-1].
Step 3: get f[n]
'''

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib_li = [0, 1]
        for i in range(2, n+1):
            fib_li.append(fib_li[i-2] + fib_li[i-1])

        return fib_li[n]
