from typing import List
class Solution :
    def median_of_two_arrays(self,nums1:list[int],nums2:List[int]):
        if len(nums1)> len(nums2):
            nums1 , nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        med = (n+m+1)//2
        l , r = 0 , len(nums1)
        while(l <= r):
            left1 = l +(r-l)//2
            left2 = med - left1

            max1 = nums1[left1-1] if left1>0 else float('-inf')
            max2 = nums2[left2-1] if left2 >0 else float('-inf')
            min1 = nums1[left1] if left1<m else float('inf')
            min2 = nums2[left2] if left2<n else float('inf')

            if max1<=min2 and max2 <=min1:
                if (m+n)%2==0:
                    return (max(max1,max2)+ min(min1,min2))/2 
                else:
                    return max(max1, max2)
            elif max1> min2:
                r = left1-1
            else:
                l = left1+1
            
