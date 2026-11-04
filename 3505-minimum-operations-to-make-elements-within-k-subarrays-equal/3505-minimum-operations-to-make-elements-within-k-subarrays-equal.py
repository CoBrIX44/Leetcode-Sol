from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}  
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(i, c, s):
            while i <= m:
                cnt[i] += c
                sm[i] += s
                i += i & -i

        def prefix(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        top = 1
        while top * 2 <= m:
            top *= 2

        def kth(kk):
            pos = 0
            step = top
            while step:
                if pos + step <= m and cnt[pos + step] < kk:
                    pos += step
                    kk -= cnt[pos]
                step >>= 1
            return pos + 1

        cost = [0] * (n - x + 1)
        total = 0
        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                r = kth((x + 1) // 2)
                med = vals[r - 1]
                cl, sl = prefix(r)
                cost[i - x + 1] = med * cl - sl + (total - sl) - med * (x - cl)

        INF = float('inf')
        prev = [0] * (n + 1)  
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x and prev[i - x] < INF:
                    v = prev[i - x] + cost[i - x]
                    if v < cur[i]:
                        cur[i] = v
            prev = cur

        return prev[n]