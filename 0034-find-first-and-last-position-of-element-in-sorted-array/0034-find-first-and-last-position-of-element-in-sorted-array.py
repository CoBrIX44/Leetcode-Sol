class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_left):
            lo, hi = 0, len(nums) - 1
            result = -1
            
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    result = mid
                    if is_left:
                        hi = mid - 1  
                    else:
                        lo = mid + 1  
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            return result
        
        left = find_bound(True)
        if left == -1:
            return [-1, -1]
        
        right = find_bound(False)
        return [left, right]