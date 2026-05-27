class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            # add not closing brackets to stack
            if s[i] != ']':
                stack.append(s[i])
            else:
                # we reset substr each time
                substr = ""
                # every [ can only have a number or another [ outside of it, not a character
                # second while checks if there is a digit to the left meaning a k existed to the left previous substr and has to be multiplied
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() # this pops opening bracket 
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k # since k is a character, 
                                        # we are just adding the CHARACTERS
                                        # not the numeric value, in reverse order
                stack.append(int(k) * substr)
        return "".join(stack)
        