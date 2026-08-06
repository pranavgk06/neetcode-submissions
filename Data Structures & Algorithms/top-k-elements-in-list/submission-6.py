class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        count = Counter(nums)

        for num,freq in count.items():
            heapq.heappush(min_heap, (freq,num))
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [y for x,y in min_heap]