class Solution:
    def sort_color(nums:list):
        low , high = -1, len(nums)
        i =0
        while i< high:
            if nums[i] == 0:
                nums[low+1], nums[i] = nums[i], nums[low+1]
                low+=1
                i+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[i] , nums[high-1] = nums[high-1], nums[i]
                high-=1