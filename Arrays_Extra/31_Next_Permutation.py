class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        pivot = None
        r = len(nums)-2
        while r >=0:
            if nums[r]<nums[r+1]:
                pivot = r
                break
            r-=1
        l , r = 0 , len(nums)-1
        if pivot is not None:
            for i in range(len(nums)-1,pivot,-1):
                if nums[i]>nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
            l = pivot +1
        while l<=r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        