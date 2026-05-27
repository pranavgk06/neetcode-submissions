class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_val = 0
        for i in range(len(s) - 1):
            val = abs(ord(s[i]) - ord(s[i+1]))
            sum_val += val
        return sum_val

        