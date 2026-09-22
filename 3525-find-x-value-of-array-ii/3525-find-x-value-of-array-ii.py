from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        # Calculate power-of-2 size for segment tree base
        M = 1
        while M < n:
            M <<= 1
            
        # Identity node for segment tree operations
        I_node = (1, [0] * k)
        tree = [I_node] * (2 * M)
        
        def merge(node1, node2):
            p1, c1 = node1
            p2, c2 = node2
            p = (p1 * p2) % k
            c = list(c1)
            for r2 in range(k):
                cnt = c2[r2]
                if cnt:
                    c[(p1 * r2) % k] += cnt
            return (p, c)

        # Initialize leaves
        for i in range(n):
            v = nums[i] % k
            cnts = [0] * k
            cnts[v] = 1
            tree[M + i] = (v, cnts)
            
        # Build segment tree
        for i in range(M - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])
            
        ans = []
        for idx, val, start, x in queries:
            # 1. Update nums[idx] = val
            v = val % k
            pos = M + idx
            cnts = [0] * k
            cnts[v] = 1
            tree[pos] = (v, cnts)
            
            pos >>= 1
            while pos > 0:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos >>= 1
                
            # 2. Query suffix range [start, n - 1]
            L = M + start
            R = M + n - 1
            res_left = I_node
            res_right = I_node
            
            while L <= R:
                if L & 1:
                    res_left = merge(res_left, tree[L])
                    L += 1
                if not (R & 1):
                    res_right = merge(tree[R], res_right)
                    R -= 1
                L >>= 1
                R >>= 1
                
            res = merge(res_left, res_right)
            ans.append(res[1][x])
            
        return ans