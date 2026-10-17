class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        def digit_sum(x):
            return sum(int(d) for d in str(x))
        
        order = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or order[i] == i:
                continue
            
            length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = order[j]
                length += 1
            
            swaps += length - 1
        
        return swaps