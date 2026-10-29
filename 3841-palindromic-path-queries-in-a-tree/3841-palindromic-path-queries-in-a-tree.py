class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        LOG = 17
        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        base = [0] * n          
        size = [1] * n
        order = []
        
        cur = [ord(c) - 97 for c in s]
        
        stack = [0]
        base[0] = 1 << cur[0]
        while stack:
            u = stack.pop()
            tin[u] = len(order) + 1   
            order.append(u)
            for w in adj[u]:
                if w != parent[u]:
                    parent[w] = u
                    depth[w] = depth[u] + 1
                    base[w] = base[u] ^ (1 << cur[w])
                    stack.append(w)
        
        for u in reversed(order):
            if parent[u] != -1:
                size[parent[u]] += size[u]
        
        up = [[0] * n for _ in range(LOG)]
        for v in range(n):
            up[0][v] = parent[v] if parent[v] != -1 else v
        for k in range(1, LOG):
            prev, row = up[k - 1], up[k]
            for v in range(n):
                row[v] = prev[prev[v]]
        
        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for k in range(LOG):
                if diff >> k & 1:
                    a = up[k][a]
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]
        
        bit = [0] * (n + 2)
        
        def add(i, d):
            while i <= n:
                bit[i] ^= d
                i += i & -i
        
        def get(i):
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r
        
        def path_mask(v):
            return base[v] ^ get(tin[v])
        
        answer = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = ord(parts[2]) - 97
                delta = (1 << cur[u]) ^ (1 << c)
                if delta:
                    add(tin[u], delta)
                    add(tin[u] + size[u], delta)   
                    cur[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = path_mask(u) ^ path_mask(v) ^ (1 << cur[l])
                answer.append(mask & (mask - 1) == 0)
        
        return answer