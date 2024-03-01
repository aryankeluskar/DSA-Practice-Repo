class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = [False]*len(matrix)
        cols = [False]*len(matrix[0])
        print(rows)
        print(cols)
        print("---")

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True 
                    pass

        print(rows)
        print(cols)

        for i in range(len(rows)):
            if rows[i]:
                matrix[i] = [0]*len(cols)

        for i in range(len(cols)):
            if cols[i]:
                for j in range(len(rows)):
                    matrix[j][i] = 0