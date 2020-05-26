class Board:
    def __init__(self):
        self.squares = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = 1
        self.winner = 0
        self.stalemate = False

    @staticmethod
    def get_player_string_value(player):
        strings = {0: '-', 1: 'O', 2: 'X'}
        return strings.get(player, ' ')

    def get_square_string_value(self, x, y):
        return self.get_player_string_value(self.squares[y][x])

    def is_game_over(self):
        return self.winner or self.stalemate

    def show(self):
        print('')
        for y in range(0, 3):
            row = ''
            for x in range(0, 3):
                row += self.get_square_string_value(x, y) + ' '
            print(row)
        print('')
        if self.winner:
            print('The `' + self.get_player_string_value(self.winner) + '` player has won!')
        elif self.stalemate:
            print('The game is a stalemate!')
        else:
            print('It is the `' + self.get_player_string_value(self.player) + '` player\'s turn')

    def place_counter(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Position is not valid!')
            return False

        if self.squares[y][x] != 0:
            print('Position is already occupied!')
            return False

        if self.is_game_over():
            print('The game is over!')
            return False

        self.squares[y][x] = self.player
        self.winner = self.player if self.check_for_winner() else self.winner
        self.stalemate = self.check_stalemate()
        self.player = 1 if self.player == 2 else 2
        return self.is_game_over()

    def check_stalemate(self):
        for y in range(0, 3):
            for x in range(0, 3):
                if self.squares[y][x] == 0:
                    return False
        return True

    def check_for_winner(self):
        win_diagonal = [True, True]
        for a in range(0, 3):
            win_diagonal[0] = win_diagonal[0] & (self.squares[a][a] == self.player)
            win_diagonal[1] = win_diagonal[1] & (self.squares[a][2 - a] == self.player)
            win_col_row = [True, True]
            for b in range(0, 3):
                win_col_row[0] = win_col_row[0] & (self.squares[a][b] == self.player)
                win_col_row[1] = win_col_row[1] & (self.squares[b][a] == self.player)
            if True in win_col_row:
                return True
        return True in win_diagonal


def play():
    board = Board()

    while True:
        board.show()

        try:
            i = int(input('Choose Column (1 to 3): '))
            j = int(input('Choose Row (1 to 3): '))

            if board.place_counter(int(i) - 1, int(j) - 1):
                board.show()
                break
        except ValueError:
            print('Invalid co-ordinates')


play()
while True:
    play_again = input('Game over, play again (y/n): ')
    if play_again.lower() == 'y':
        play()
    elif play_again.lower() == 'n':
        break
