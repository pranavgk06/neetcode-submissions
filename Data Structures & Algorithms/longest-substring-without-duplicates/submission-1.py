class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        max_len = 0 # tracks max length across each iteration 
        window = set()

        for r in range(len(s)):
            while s[r] in window: # when constraint isnt met, remove from window until no more s[r]
                window.remove(s[l])
                l+=1 
            window.add(s[r]) # when constraint is met, keep adding to max length 
            max_len = max(max_len, r - l + 1) #standard of finding max 
        return max_len