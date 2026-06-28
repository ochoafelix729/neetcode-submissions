from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums = []
        decreasing_q = deque([])
        l = 0
        for r in range(len(nums)):
            while len(decreasing_q) > 0 and nums[r] > decreasing_q[-1]:
                decreasing_q.pop()
            decreasing_q.append(nums[r])
            if (r - l + 1) == k:
                maximums.append(decreasing_q[0])
                if nums[l] == decreasing_q[0]:
                    decreasing_q.popleft()
                l += 1
        return maximums



