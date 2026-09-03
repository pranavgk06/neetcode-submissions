class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()

        def backtrack(index,remaining):
            if remaining < 0:
                return
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, remaining - candidates[i])
                path.pop()
        
        backtrack(0, target)
        return result
        