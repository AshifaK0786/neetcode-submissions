class Solution:
    def spiralOrder(self, matrix):
        ans = []

        while matrix:
            ans+=matrix.pop(0)
            if matrix:
                matrix=list(zip(*matrix))[::-1]
        return ans