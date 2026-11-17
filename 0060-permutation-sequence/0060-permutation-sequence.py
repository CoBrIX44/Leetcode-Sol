class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n + 1)]
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        
        k -= 1 
        result = []
        
        for i in range(n, 0, -1):
            block = fact[i - 1]      
            index = k // block
            result.append(digits.pop(index))
            k %= block
        
        return ''.join(result)