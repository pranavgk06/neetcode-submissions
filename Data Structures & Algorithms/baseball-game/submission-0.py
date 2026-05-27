class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        count = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                plus = stack[-1] + stack[-2]
                stack.append(plus)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                double = 2 * stack[-1]
                stack.append(double)
            else:
                stack.append(int(operations[i]))

        while stack:
             count += stack.pop()
        return count
        