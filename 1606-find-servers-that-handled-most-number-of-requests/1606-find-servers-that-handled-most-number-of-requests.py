import heapq
from bisect import bisect_left
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = SortedList(range(k))   
        busy = []                     
        count = [0] * k
        
        for i in range(len(arrival)):
            t = arrival[i]
            
            while busy and busy[0][0] <= t:
                _, s = heapq.heappop(busy)
                free.add(s)
            
            if not free:
                continue  
            
            pos = free.bisect_left(i % k)
            if pos == len(free):
                pos = 0
            s = free[pos]
            
            free.remove(s)
            heapq.heappush(busy, (t + load[i], s))
            count[s] += 1
        
        best = max(count)
        return [i for i in range(k) if count[i] == best]