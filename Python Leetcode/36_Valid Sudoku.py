from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = [set() for _ in range(9)]
        cols_seen = [set() for _ in range(9)]
        subgrids_seen = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if val in rows_seen[r]:

                    return False
                rows_seen[r].add(val)

                if val in cols_seen[c]:

                    return False
                cols_seen[c].add(val)

                subgrid_idx = (r // 3) * 3 + (c // 3)
                if val in subgrids_seen[subgrid_idx]:

                    return False
                subgrids_seen[subgrid_idx].add(val)

        return True