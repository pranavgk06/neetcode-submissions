class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start+1, len(s) + 1):
                piece = s[start:end]
                if palindrome(piece):
                    path.append(piece)
                    backtrack(end)
                    path.pop()
        backtrack(0)
        return result
        