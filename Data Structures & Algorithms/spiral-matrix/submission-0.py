class Solution:
    def spiralOrder(self, matrix):
        ans = []

        while matrix:
            # Take the first row
            ans += matrix.pop(0)

            # Rotate the remaining matrix
            if matrix:
                matrix = list(zip(*matrix))[::-1]

        return ans