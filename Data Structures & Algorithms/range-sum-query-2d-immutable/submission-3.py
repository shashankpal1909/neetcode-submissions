class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * cols for _ in range(rows)]

        self.prefix[0][0] = matrix[0][0]

        # first column
        for r in range(1, rows):
            self.prefix[r][0] = self.prefix[r - 1][0] + matrix[r][0]

        # first row
        for c in range(1, cols):
            self.prefix[0][c] = self.prefix[0][c - 1] + matrix[0][c]

        # remaining cells
        for r in range(1, rows):
            for c in range(1, cols):
                self.prefix[r][c] = (
                    matrix[r][c]
                    + self.prefix[r - 1][c]
                    + self.prefix[r][c - 1]
                    - self.prefix[r - 1][c - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]

        if row1 > 0:
            total -= self.prefix[row1 - 1][col2]
        if col1 > 0:
            total -= self.prefix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            total += self.prefix[row1 - 1][col1 - 1]

        return total
