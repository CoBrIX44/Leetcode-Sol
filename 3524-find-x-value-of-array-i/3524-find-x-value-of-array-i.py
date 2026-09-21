class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        cur = [0] * k  
        
        for num in nums:
            r = num % k
            new_cur = [0] * k
            
            for rem in range(k):
                if cur[rem]:
                    new_cur[(rem * r) % k] += cur[rem]
           
            new_cur[r] += 1
            
            cur = new_cur
            for x in range(k):
                result[x] += cur[x]
        
        return result