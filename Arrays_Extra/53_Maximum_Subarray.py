class Solution:
    def max_subarray(nums:list)->int:
        m_sum = float('-inf')
        sum_c =0
        for i in range(len(nums)):
            sum_c += nums[i]
            if nums[i]> sum:
                sum_c = nums[i]
            m_sum = max(sum_c , m_sum)
        return m_sum
               
