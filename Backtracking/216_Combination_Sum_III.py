class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        path = []
        result =[]
        def helper(total ,index):
            if total==n and len(path)==k:
                result.append(path[:])
                return
            if len(path)==k:
                return
            if total>n:
                return
            for i in range(index,10):
                path.append(i)
                total+=i
                helper(total,i+1)
                path.pop()
                total-=i
        helper(0,1)
        return result