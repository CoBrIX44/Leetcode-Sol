import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]  
        heapq.heapify(free)
        busy = []  
        ans = []
        time = 0
        
        for j in range(len(tasks)):
            time = max(time, j)
            
            if not free:
                time = max(time, busy[0][0])
            
            while busy and busy[0][0] <= time:
                t, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            
            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (time + tasks[j], w, i))
        
        return ans