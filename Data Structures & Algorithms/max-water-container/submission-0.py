class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        area = -1
        while i < j:
            width = j-i
            max_area = max(area, width * min(heights[i], heights[j]))
            area = max_area 
            if heights[i] <= heights[j]:
                i+=1
            elif heights[j] <= heights[i]:
                j-=1
        return max_area

        