class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while True:
            guess = numbers[l] + numbers[r]
            if guess == target:
                return [l+1, r+1]
            if guess < target:
                l += 1
            else:
                r -= 1