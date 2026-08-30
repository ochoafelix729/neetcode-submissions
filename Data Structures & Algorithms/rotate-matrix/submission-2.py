class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix) - 1
        while left < right:
            bottom, top = right, left
            for i in range(right - left):
                top_left = matrix[top][left + i]

                # left -> top
                matrix[top][left + i] = matrix[bottom - i][left]

                # bottom -> left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # right -> bottom
                matrix[bottom][right - i] = matrix[top + i][right]

                # top -> right
                matrix[top + i][right] = top_left

            left += 1
            right -= 1
        