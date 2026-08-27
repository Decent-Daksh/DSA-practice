"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""
from typing import List
class Solution:
    def longest_repeating_char_replace(self, s, k):
        max_length = 0
        maxi = 0
        window = {}
        l = 0
        for r in range (len(s)):
            window[s[r]] = window.get(s[r],0) +1
            maxi = max(maxi , window[s[r]])
            while r-l+1 - maxi > k:
                window[s[l]] -= 1
                l += 1
            max_length = max(max_length , r-l+1)
        return max_length