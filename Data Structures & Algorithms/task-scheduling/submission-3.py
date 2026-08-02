class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-s for s in count.values()]
        heapq.heapify(maxheap)
        time = 0
        q = deque()

        while maxheap or q:
            time += 1
            if not maxheap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q:
                if time == q[0][1]:
                    heapq.heappush(maxheap, q.popleft()[0])
        return time
        