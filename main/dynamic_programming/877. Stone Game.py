"""
https://leetcode.com/problems/stone-game/description/

Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.
Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.
Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.


Example 1:
Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.


Example 2:
Input: piles = [3,7,2,3]
Output: true
"""


'''
Note from Hottari

'''

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        def pick(l, r):
            if l > r: return 0                      # End point
            if (r-l)%2:                             # Alice's Turn 
                return max(piles[l] + pick(l+1, r), 
                           piles[r] + pick(l, r-1))
            else:                                   # Bob's Turn
                return min(-piles[l] + pick(l+1, r), 
                           -piles[r] + pick(l, r-1))

        return ( pick(0, len(piles)-1) > 0 )   
    


# imporced by GPT

class Solution2(object):
    def stoneGame(self, piles):
        """
        Determine whether Alice can win the stone game when both players play optimally.

        :type piles: List[int]
        :param piles: A list of positive integers representing the number of stones in each pile.

        :rtype: bool
        :return: True if Alice can win the game, False otherwise.
        """
        n = len(piles)  
        dp = [[0] * n for _ in range(n)]  

        for i in range(n): dp[i][i] = piles[i]                  # Initialize the DP table for single piles (base case)
        
        for length in range(2, n + 1):                          # Fill in the DP table for different pile lengths
            for l in range(n - length + 1):
                r = l + length - 1
                dp[l][r] = max(piles[l] - dp[l + 1][r], piles[r] - dp[l][r - 1]) # Calculate the optimal value for the current subproblem

        # The result in dp[0][n - 1] represents the maximum difference
        # between Alice and Bob's total values, and if it's positive,
        # Alice wins; otherwise, Bob wins.
        return dp[0][n - 1] > 0