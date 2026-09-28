class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 3):
            # skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # skip duplicates for the third number
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
        
        return result