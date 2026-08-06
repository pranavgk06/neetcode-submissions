class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        groups = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in groups:
                groups[key].append(strs[i])
            else:
                groups[key] = [strs[i]] 

        for key in groups:
            output.append(groups[key])
        return output    