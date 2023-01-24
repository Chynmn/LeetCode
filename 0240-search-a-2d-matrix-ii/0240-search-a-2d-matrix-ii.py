class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for chk in matrix:
            print(chk)
            if target in chk:
                return True
        return False