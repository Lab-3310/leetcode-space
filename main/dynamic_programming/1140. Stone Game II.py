"""
https://leetcode.com/problems/moving-stones-until-consecutive-ii/


Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104

"""

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        prefix_sum = [0] * (n + 1)                  # Initialize a prefix sum array for efficient subarray sum calculations
        dp = {}                                     # Memoization dictionary to store computed results

        for i in range(n - 1, -1, -1):              # Calculate prefix sum from right to left
            prefix_sum[i] = prefix_sum[i + 1] + piles[i]
 
        def dfs(i, M):                              # Recursive function to explore all possible moves and calculate the optimal score
            
            res = float("-inf")                     # Initialize the maximum score for the current state for Bob turn     
            if i == n: return 0                     # Base case: If all piles are processed, return 0
            if (i, M) in dp: return dp[(i, M)]      # Memoization check: Return memoized result if available
 
            for X in range(1, 2 * M + 1):           # Explore all possible choices of X (number of piles to take)
                if i + X > n:  break
                opponent_best = dfs(i + X, max(M, X))                   # Calculate the opponent's best move by recursively calling dfs
                current_score = prefix_sum[i] - opponent_best           # Calculate the current player's score
                res = max(res, current_score)
            dp[(i, M)] = res                        # Memoize the result for the current state

            return res
        
        return dfs(i=0, M=1)                        # Call the dfs function with initial parameters i=0 and M=1


"""
class Solution(object):
    def stoneGameII(self, piles):
    
        dp = {}
        def dfs(alice, i, M):
            if i==len(piles): return 0
            if (alice, i, M) in dp: return dp[(alice, i, M)]

            res = 0 if alice else float("inf")
            total = 0
            for X in range(1, M*2+1):
                if i+X > len(piles): break
                total += piles[i+X-1]

                if alice: res = max(res, total + dfs(not alice, i+X, max(M, X)))
                else:     res = min(res, dfs(not alice, i+X, max(M, X)))
            
            dp[(alice, i, M)] = res
            return res

        return dfs(alice=True, i=0, M=1)

"""
        