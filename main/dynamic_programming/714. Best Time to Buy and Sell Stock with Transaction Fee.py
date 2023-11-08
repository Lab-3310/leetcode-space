"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.



Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        not_buy = 0
        buy = 0

        n = len(prices)
        for i in range(n-1, 0-1, -1):
            cur_not_buy = max(prices[i] + buy,  0 + not_buy)
            cur_buy = max(-prices[i] - fee + not_buy, 0 + buy)
            
            buy = cur_buy
            not_buy = cur_not_buy
       
        return buy


"""
Sol 2.

class Solution(object):
    def maxProfit(self, prices, fee):

        pos = -prices[0]
        profit = 0

        n = len(prices)
        for i in range(1, n):
            pos = max(pos, profit - prices[i])
            profit = max(profit, pos + prices[i] - fee)

        return profit

"""

        