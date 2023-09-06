"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


'''
Note from Hottari

Sol. I
(We cannot rob two neighboring houses)
1. Find the maximum of the previous 2 houses (i-1, i-2) (if length >= 3).
2. Compare the maximum of 'i-2 + i' and 'i-1' (Check if it's better to rob the ith house).

To accomplish this, we can maintain 2 numbers to store the values of the previous 2 houses (called 'max0' and 'max1'). 
We'll then determine the maximum between 'max0 + current house' and 'max1'.

Step 0: For the previous 2 houses -> Initialize max0 = nums[0], max1 = max(nums[:2]).
Step 1: Evaluate whether it's better to rob the current house -> rob_max = max(max0 + i, max1).
Step 2: update max0, max1

'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenth = len(nums)
        if lenth > 2:                       
            max0 = nums[0]
            max1 = max(nums[:2])
            for i in nums[2:]:
                rob_max = max(max0 + i, max1)   # evaluate whether it's better to rob the current house
                max0 = max1                     # update max0, max1
                max1 = rob_max
            return rob_max
        
        return max(nums) #elif 1 <= lenth <= 2: rob_max = max(nums)   