from cell import Cell


class Board:
    def __init__(self):
        self.field = [Cell(i) for i in range(9)]

    def display_board(self):
        print('-------------')
        for i in range(0, 9, 3):
            print(f'| {self.field[i].symbol} | {self.field[i + 1].symbol} | {self.field[i + 2].symbol}')
        print('-------------')

    def change_cell(self, cell_number, symbol):
        cell = self.field[cell_number - 1]
        if cell.occupied:
            return False
        cell.symbol = symbol
        cell.occupied = True
        return True

    def check_game_over(self):
        win_position = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for pos in win_position:
            if (self.field[pos[0]].symbol != " " and self.field[pos[0]].symbol ==
                    self.field[pos[1]].symbol == self.field[pos[2]].symbol):
                return True
        return False

    def reset_board(self):
        for cell in self.field:
            cell.symbol = ' '
            cell.occupied = False

