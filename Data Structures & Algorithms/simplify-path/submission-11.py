class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = "" # tells us current file or path we are in 

        for c in path + "/":
            if c == "/":
                if cur == "..": #pop from stack if non empty
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".": #excludes only empty token and the other special token of . which represents current directory
                    stack.append(cur)
                cur = "" #reset current token because we finished processing
            else:
                cur += c #building file name

        return "/" + "/".join(stack)