class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        l, h = 0, r * c - 1

        while l <= h:
            mid = (l + h) // 2

            x = matrix[mid // c][mid % c]

            if x == target:
                return True
            elif x < target:
                l = mid + 1
            else:
                h = mid - 1

        return False