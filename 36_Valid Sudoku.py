class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[]
        col=[]
        for _ in range(9):
            row.append([0,0,0,0,0,0,0,0,0])
            col.append([0,0,0,0,0,0,0,0,0])

        grid = [[[] for _ in range(3)] for _ in range(3)]

        for i in range(9):  
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j]:
                    return False
                if board[i][j] in grid[i//3][j//3]:
                    return False
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                grid[i//3][j//3].append(board[i][j])

        return True 