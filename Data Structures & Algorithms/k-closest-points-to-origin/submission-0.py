class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        arr = []

        for x,y in points:
            distance = (x**2 + y**2)
            heapq.heappush(max_heap, (-distance,x,y))
            while len(max_heap) > k:
                heapq.heappop(max_heap)
        
        while max_heap:
            distance,x,y = heapq.heappop(max_heap)
            arr.append([x,y])
        return arr
        