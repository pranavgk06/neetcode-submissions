class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        stack = []
        max_val = 0
        for i in range(len(s)):
            if stack and s[i] == ')':
                stack.pop()
                count -=1
            elif s[i] != '(':
                continue
            else:
                stack.append(s[i])
                count+=1
                max_val = max(max_val, count)
        return max_val
            
            
        