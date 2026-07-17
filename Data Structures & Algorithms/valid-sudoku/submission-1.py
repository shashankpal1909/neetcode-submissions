class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_row(row: int, col: int, val: str) -> bool:
            for i in range(9):
                if i != col and board[row][i] == val:
                    return False

            return True

        def check_col(row: int, col: int, val: str) -> bool:
            for i in range(9):
                if i != row and board[i][col] == val:
                    return False

            return True

        def get_section_start(row: int, col: int) -> tuple[int, int]:

            sections = [
                (0, 0),
                (0, 3),
                (0, 6),
                (3, 0),
                (3, 3),
                (3, 6),
                (6, 0),
                (6, 3),
                (6, 6),
            ]

            for section in sections:
                if section[0] <= row <= section[0] + 2 and section[1] <= col <= section[1] + 2:
                    return section

            return sections[0]

        def check_section(row: int, col: int, val: str) -> bool:
            x, y = get_section_start(row, col)

            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if not (i == row and j == col) and board[i][j] == val:
                        return False

            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not check_row(i, j, board[i][j]):
                        return False
                    if not check_col(i, j, board[i][j]):
                        return False
                    if not check_section(i, j, board[i][j]):
                        return False

        return True
