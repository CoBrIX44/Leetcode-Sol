class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        
        for a in arr1:
            ok = True
            for b in arr2:
                if abs(a - b) <= d:
                    ok = False
                    break
            if ok:
                count += 1
        
        return count