class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        need_count = len(need)
        start = 0
        window = dict()
        l = 0
        min_len = float("inf")
        have = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in need and window[s[r]] == need[s[r]]:
                have+=1
            
            while have == need_count:
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    start = l
                window[s[l]] -=1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have-=1
                l+=1
        
        if min_len == float("inf"):
            return ""
        else:
            return s[start:start+min_len]

