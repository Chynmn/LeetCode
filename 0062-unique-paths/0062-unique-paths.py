
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i][j-1] + arr[i-1][j]
        return arr[m-1][n-1]