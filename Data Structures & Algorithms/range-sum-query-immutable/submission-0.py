class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        running = 0
        for n in nums:
            self.prefixSum.append(running + n)
            running += n

    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefixSum[left - 1] if left > 0 else 0
        rightSum = self.prefixSum[right]
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)