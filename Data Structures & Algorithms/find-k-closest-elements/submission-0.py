class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        best_left = l
        window = []
        for r in range(len(arr)):
            window.append(arr[r])
            if (r - l + 1) > k:
                l += 1
                if abs(arr[r] - x) < abs(window.pop(0) - x):
                    best_left = l

        return arr[best_left:best_left+k]

