from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        res = []
        step = 1
        index = 1
        totalcells = rows*cols
        res.append([rStart, cStart])

        while index < totalcells:
            # motion left to right
            for _ in range(step):
                cStart += 1
                if 0 <= cStart < cols and 0 <= rStart < rows:
                    res.append([rStart, cStart])
                    index += 1
            # motion top to bottom
            for _ in range(step):
                rStart += 1
                if 0 <= cStart < cols and 0 <= rStart < rows:
                    res.append([rStart, cStart])
                    index += 1
            # motion right to left
            step +=1
            for _ in range(step):
                cStart -= 1
                if 0 <= cStart < cols and 0 <= rStart < rows:
                    res.append([rStart, cStart])
                    index += 1
            for _ in range(step):
                rStart -= 1
                if 0 <= cStart < cols and 0 <= rStart < rows:
                    res.append([rStart, cStart])
                    index += 1
            step +=1

        return res


sol = Solution()

val = sol.spiralMatrixIII(3, 4, 1, 2)
print(val)
