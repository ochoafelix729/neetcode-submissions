class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # on line 17, we can't set a res array to window because then 
        #   res and window reference the same list
        # we shouldn't do res = window.copy() either because this is O(n) time
        # instead we keep track of the best starting index for our possible windows

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