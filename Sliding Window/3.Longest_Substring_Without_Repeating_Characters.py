#3. Longest Substring Without Repeating Characters

#Given a string s, find the length of the longest substring without duplicate characters.

 

#Example 1:

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
#Example 2:

#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:

from typing import List

class Solution:
    def longest_substring_without_repeat(self, s):
        max_length = 0
        window ={}
        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0) + 1
            while window[s[right]]>1:
                window[s[left]] = window.get(s[left]) -1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            max_length = max( max_length , right-left+1)

        return max_length
 