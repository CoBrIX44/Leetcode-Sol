class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = {}
        
        def dfs_find_parents(u):
            char = s[u]
            prev_ancestor = last_seen.get(char, -1)
            
            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor
                
            last_seen[char] = u
            
            for v in adj[u]:
                dfs_find_parents(v)
                
            last_seen[char] = prev_ancestor

        dfs_find_parents(0)
        
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        answer = [1] * n
        
        def dfs_sizes(u):
            total = 1
            for v in new_adj[u]:
                total += dfs_sizes(v)
            answer[u] = total
            return total
            
        dfs_sizes(0)
        return answer