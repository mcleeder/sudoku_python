class Sudoku():
    def __init__(self, byte_string: bytes | None = None) -> None:
        if byte_string:
            self.board = self._decode_form_data(byte_string)
        else:
            self.board = [[0 for _ in range(9)] for _ in range(9)]

    def _decode_form_data(self, byte_string: bytes) -> list[list[int]]:
        values_str = byte_string.decode('utf-8')
        rows = values_str.strip().split(',')
        return [list(map(int, rows[i:i+9])) for i in range(0, len(rows), 9)]

    def solve(self):
        """
        Solver
        """
        if not self._valid_board():
            return False

        solved = False
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    for guess in range(1, 10):
                        if self._valid_guess((x, y), guess):
                            self.board[y][x] = guess
                            if self.solve():
                                solved = True
                                break
                            self.board[y][x] = 0
                    return True if solved else False
        return True

    def _valid_guess(self, cell: tuple[int], n: int) -> bool:
        x, y = cell
        if any([self._num_in_column(n, x), self._num_in_row(n, y)]):
            return False

        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if self.board[y0+i][x0+j] == n:
                    return False
        return True

    def _get_column(self, col: int) -> list[int]:
        return [x[col] for x in self.board]

    def _get_row(self, row: int) -> list[int]:
        return self.board[row]

    def _num_in_column(self, n: int, i: int) -> bool:
        return self._get_column(i).count(n) > 1

    def _num_in_row(self, n: int, i: int) -> bool:
        return self._get_row(i).count(n) > 1

    def _valid_column_solution(self, col: int) -> bool:
        return sum(self._get_column(col)) == 45

    def _valid_row_solution(self, row: int) -> bool:
        return sum(self._get_row(row)) == 45
    
    def _valid_board_solution(self) -> bool:
        valid_rows = all([self._valid_row_solution(n) for n in range(9)])
        valid_cols = all([self._valid_column_solution(n) for n in range(9)])
        return all([valid_cols,valid_rows])
    
    def _valid_board(self) -> bool:
        for y in range(9):
            for x in range(9):
                num = self.board[y][x]
                if num == 0:
                    continue
                if (self._get_column(x).count(num) > 1) or (self._get_row(y).count(num) > 1):
                    return False
        return True
    
    def solved(self):
        return self._valid_board_solution()
    
    def print(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))




