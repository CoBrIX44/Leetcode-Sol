from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        dq = deque()  
        cost = 0
        r = n - 1
        ans = 0

        for l in range(n - 1, -1, -1):
            while dq and dq[0][1] <= nums[l]:
                p, v = dq.popleft()
                end = dq[0][0] - 1 if dq else r
                cost -= v * (end - p + 1) - (pre[end + 1] - pre[p])

            dq.appendleft((l, nums[l]))
            end = dq[1][0] - 1 if len(dq) > 1 else r
            cost += nums[l] * (end - l + 1) - (pre[end + 1] - pre[l])

            while cost > k:
                cost -= dq[-1][1] - nums[r]
                if dq[-1][0] == r:
                    dq.pop()
                r -= 1

            ans += r - l + 1

        return ans