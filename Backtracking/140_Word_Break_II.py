class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)
        path =[]
        result =[]
        def solver(index):
            if index==len(s):
                result.append(' '.join(path))
                return
            word=""
            for i in range(index , len(s)):
                word = word+s[i]
                if word in words:
                    path.append(word)
                    solver(i+1)
                    path.pop()
            return
        solver(0)
        return result
        


     
        