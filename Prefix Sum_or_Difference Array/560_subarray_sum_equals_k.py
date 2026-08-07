class Solutions:
    def subarray_sum_equals_k(self , nums,k):
        count = 0
        prefix_sum = 0
        seen ={0:1}
        for num in nums:
            prefix_sum += num
            count += seen.get(prefix_sum - k , 0)
            seen[prefix_sum] = seen.get(prefix_sum , 0) +1
        return count