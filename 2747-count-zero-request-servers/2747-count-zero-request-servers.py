from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        
        count = [0] * (n + 1)  
        active = 0             
        left = right = 0       
        result = [0] * len(queries)
        
        for qi in order:
            q = queries[qi]
            
            while right < len(logs) and logs[right][1] <= q:
                s = logs[right][0]
                if count[s] == 0:
                    active += 1
                count[s] += 1
                right += 1
            
            while left < right and logs[left][1] < q - x:
                s = logs[left][0]
                count[s] -= 1
                if count[s] == 0:
                    active -= 1
                left += 1
            
            result[qi] = n - active
        
        return result