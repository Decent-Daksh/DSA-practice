class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        path = []
        result =[]
        nums = sorted(nums)
        def helper(index):
            if len(path)<=len(nums):
                result.append(path[:])
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                else:
                    path.append(nums[i])
                    helper(i+1)
                    path.pop()
        helper(0)
        return result