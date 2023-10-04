"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally

https://leetcode.com/problems/divisor-game/
 

Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
"""



'''
Note from Hottari

Sol. I  
(define initial value: If n equals 1, the result is False.)
(when "rival loses," it means I win.)
(new result is from the previous result.)
(check only up to the square root of i.)

Step 1: div[1] = 0  -> loop start from 2
Step 2: rivel lose means we wins -> if (i%j==0) and (div[i-j]==0): div[i]=1
Step 3: loop through j  only up to sqrt(i) (factor is pair)
'''

class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        div = [0]*(n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                if j*j > i: break                   # exit loop
                if (i%j==0) and (div[i-j]==0): 
                    div[i]=1
                    break
        return div[n]