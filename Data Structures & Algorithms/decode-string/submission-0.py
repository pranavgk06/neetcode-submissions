class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            # add not closing brackets to stack
            if s[i] != ']':
                stack.append(s[i])
            else:
                # checks both options, if stack[-1] is a number or string
                # if closing bracket, pop into substring
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() # this pops opening bracket 
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k #adds k in order to multiply with substr
                stack.append(int(k) * substr)
        return "".join(stack)
        