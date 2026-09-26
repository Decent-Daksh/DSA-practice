class Solution:
    def plaindrome_partitioning(self, s: str)-> list[list[str]]:
        def is_palindrome(word):
            l,r = 0 ,len(word)-1
            while l<r:
                if word[l]!=word[r]:
                    return False
                r-=1
                l+=1
            return True
        path =[]
        result=[]
        
        def solver(index):
            if index==len(s):
                result.append(path[:])
                return
            for i in range(index,len(s)):
                if is_palindrome(s[index:i+1])==False:
                    continue
                path.append(s[index,i+1])
                solver(i+1)
                path.pop()
        solver(0)
        return result
        