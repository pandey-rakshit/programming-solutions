class Solution:
    
    def convertCol(matrix: List[List[int]], j: int, m: int):
        for x in range(m):
            matrix[x][j] = 0

        return matrix

    def convertRow(matrix: List[List[int]], i: int, n: int):
        for x in range(n):
            matrix[i][x] = 0
        return matrix

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        arr = []

        for i in range (m):
            for j in range(n):
                if (matrix[i][j] == 0): 
                    arr.append((i,j))

        for x in arr:
            i = x[0]
            j = x[1]
            matrix = Solution.convertRow(matrix, i, n)
            matrix = Solution.convertCol(matrix, j, m)

        
        print(matrix)

