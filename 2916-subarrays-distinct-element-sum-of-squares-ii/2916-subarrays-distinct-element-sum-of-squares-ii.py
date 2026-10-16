class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B1 = [0] * (n + 2)
        B2 = [0] * (n + 2)

        def update(B, i, v):
            while i <= n:
                B[i] += v
                i += i & -i

        def query(B, i):
            s = 0
            while i > 0:
                s += B[i]
                i -= i & -i
            return s

        def prefix(i):
            return query(B1, i) * i - query(B2, i)

        def range_add(l, r, v):
            update(B1, l, v)
            update(B1, r + 1, -v)
            update(B2, l, v * (l - 1))
            update(B2, r + 1, -v * r)

        last = {}
        f = 0      
        total = 0

        for j in range(1, n + 1):
            x = nums[j - 1]
            l = last.get(x, 0) + 1
            r = j
            s = prefix(r) - prefix(l - 1)   
            f += 2 * s + (r - l + 1)
            total += f
            range_add(l, r, 1)
            last[x] = j

        return total % MOD