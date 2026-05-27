class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in s1:
            count[c] = count.get(c, 0) + 1
        
        window = {}
        matches = 0
        total = len(count)
        l = 0

        for r in range(len(s2)):
            # add s2[r] to window
            window[s2[r]] = window.get(s2[r], 0) + 1
            
            # check if adding s2[r] affected matches
            if window[s2[r]] == count.get(s2[r], 0):
                matches += 1  # just became equal
            elif window[s2[r]] - 1 == count.get(s2[r], 0):
                matches -= 1  # was equal, now overcounted

            # shrink window if too large
            if r - l + 1 > len(s1):
                # check if removing s2[l] affects matches before decrementing
                if window[s2[l]] == count.get(s2[l], 0):
                    matches -= 1  # was equal, about to become unequal
                elif window[s2[l]] - 1 == count.get(s2[l], 0):
                    matches += 1  # was overcounted, about to become equal
                window[s2[l]] -= 1
                l += 1

            # check if all characters match
            if matches == total:
                return True

        return False
        