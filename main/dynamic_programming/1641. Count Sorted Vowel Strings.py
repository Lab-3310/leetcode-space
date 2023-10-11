"""
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.


https://leetcode.com/problems/count-sorted-vowel-strings/description/
 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
"""



'''
Note from Hottari

Sol. I  
n=1: 'a', 'e', 'i', 'o', 'u'  
     (1 +  1  + 1  + 1  + 1)
n=2:  consider each alphabet after itself  
(1)         'uu'
(2 = 1+1)   'oo', 'ou
(3 = 2+1)   'ii', 'io', 'iu'
.
.
.
(5 + 4 + 3 + 2 + 1)

n=3  consider each n=2 pair after itself 
(1)         'uuu'
(3 = 2+1)   'ooo', 'oou',  &  'ouu'
(6 = 3+3)   'iii', 'iio', 'iiu'  &  'ioo', 'iou'  &  'iuu'
.
.
.
(15 + 10 + 6 + 3 + 1)

'''

class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """

        li = [1, 1, 1, 1, 1]
        for i in range(2, n+1):
            for j in range(1, 5): li[j] = li[j-1] + li[j]

        return sum(li)
        