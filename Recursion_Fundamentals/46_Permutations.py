from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def helper(nums, path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for num in nums:
                if num not in  path:
                    path.append(num)
                    helper(nums,path)
                    path.pop()
        helper(nums, path)
        return result