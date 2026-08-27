"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
 
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
from typing import List
class Solution:
    def min_size_subarray(self, nums , target):
        min_size = float('inf')
        total = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_size = min(min_size , right-left+1)
                total -= nums[left]
                left += 1

        return min_size if min_size != float('inf') else 0

sol = Solution()
result =sol.min_size_subarray([1,4,4] , 4)
print(result)