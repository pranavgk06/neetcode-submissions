class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        for key in groups:
            output.append(groups[key])
        return output
