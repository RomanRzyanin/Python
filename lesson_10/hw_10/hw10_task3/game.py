from board import Board


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = Board()


    def launch_move(self, player):
        while True:
            self.board.display_board()
            cell_number = player.make_move()
            if self.board.change_cell(cell_number, player.symbol):
                if self.board.check_game_over():
                    return True
                return False
            print("Клетка занята. Сделайте другой ход.")

    def play_one_game(self):
        print("Игра началась!")
        while True:
            for player in self.players:
                if self.launch_move(player):
                    self.board.display_board()
                    print(f"Поздравляем, {player.name}! Вы выиграли!")
                    player.wins += 1
                    return
                if all(cell.occupied for cell in self.board.field):
                    self.board.display_board()
                    print("Ничья!")
                    return

    def start_games(self):
        print("Добро пожаловать в игру Крестики-Нолики!")
        while True:
            self.board.reset_board()
            self.play_one_game()
            print(f'Счет: {self.players[0].name} - {self.players[0].wins}, '
                  f'{self.players[1].name} - {self.players[1].wins}')
            again = input("Хотите продолжить игру? (да/нет): ")
            if again.lower() != 'да':
                print("Спасибо за игру!")
                break
