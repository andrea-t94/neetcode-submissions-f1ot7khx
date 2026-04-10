class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        '''prefix sum of the matrix '''
        ROWS, COLS = len(matrix), len(matrix[0])
        # prefix sum left->right and top->bottom
        # offset to avoid dealing with r-1<0
        self.preMat = [[0]*(COLS+1) for _ in range(ROWS+1)]
        for r in range(ROWS):
            pref = 0
            for c in range(COLS):
                pref += matrix[r][c]
                above = self.preMat[r][c+1] #litellally the num in the row above
                self.preMat[r+1][c+1] = pref + above


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ''' prefMat of row2, col2 minus the pref sum left and above 
        we need to re-add the bottomRight corner since it is canceled out twice'''
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        topLeft = self.preMat[row2][col2]
        above = self.preMat[row1-1][col2]
        left = self.preMat[row2][col1-1]
        bottomRight = self.preMat[row1-1][col1-1]

        return topLeft - above - left + bottomRight
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)