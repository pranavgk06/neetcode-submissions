class Solution:
    def isValid(self, s: str) -> bool:
        new_stack = []
        hash_map = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c in hash_map:
                if new_stack and new_stack[-1] == hash_map[c]:
                    new_stack.pop()
                else:
                    return False
            else:
                new_stack.append(c)
        if new_stack:
            return False
        return True