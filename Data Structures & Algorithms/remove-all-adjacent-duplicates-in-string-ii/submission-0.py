class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = [] #includes [char, count]

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1]) #add character and a val of +1 to stack

            if stack[-1][1] == k:
                stack.pop()

        res = ""
        for char, count in stack:
            res += (char * count)
        return res

        


        