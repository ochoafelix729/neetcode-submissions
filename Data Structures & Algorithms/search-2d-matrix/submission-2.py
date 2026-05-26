class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        row = -1
        while low <= high:
            mid = (low+high) // 2
            el = matrix[mid][0]
            n = len(matrix[0])-1
            if matrix[mid][0] <= target <= matrix[mid][n]:
                row = mid
                break
            elif el > target:
                high = mid-1
            elif el < target:
                low = mid+1
            
        if row == -1:
            return False
        
        l, r = 0, len(matrix[row])-1
        while l <= r:
            mid = (l+r) // 2
            el = matrix[row][mid]
            if el > target:
                r = mid-1
            elif el < target:
                l = mid+1
            else:  
                return True
        
        return False



