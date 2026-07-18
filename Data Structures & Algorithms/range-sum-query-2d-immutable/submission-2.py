class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self._prefix = [[0] * n for _ in range(m)]

        self._prefix[0][0] = matrix[0][0]

        for i in range(1, m):
            self._prefix[i][0] = matrix[i][0] + self._prefix[i - 1][0]

        for i in range(1, n):
            self._prefix[0][i] = matrix[0][i] + self._prefix[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                self._prefix[i][j] = (
                    self._prefix[i - 1][j]
                    + self._prefix[i][j - 1]
                    + matrix[i][j]
                    - self._prefix[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self._prefix[row2][col2]
            + (0 if (row1 == 0 or col1 == 0) else self._prefix[row1 - 1][col1 - 1])
            - (0 if col1 == 0 else self._prefix[row2][col1 - 1])
            - (0 if row1 == 0 else self._prefix[row1 - 1][col2])
        )
