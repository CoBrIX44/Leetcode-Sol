import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        
        INF = float('inf')
        dist = {}
        dist[(0, 1)] = 0
        heap = [(0, 0, 1)]  
        
        while heap:
            d, u, run = heapq.heappop(heap)
            if dist.get((u, run), INF) < d:
                continue
            if u == n - 1:
                return d
            
            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    new_run = run + 1
                else:
                    new_run = 1
                if new_run > k:
                    continue
                nd = d + w
                if nd < dist.get((v, new_run), INF):
                    dist[(v, new_run)] = nd
                    heapq.heappush(heap, (nd, v, new_run))
        
        return -1