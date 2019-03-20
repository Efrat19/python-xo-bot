import random


class Xo:
    def __init__(self):
        self.player = None
        self.me = None
        self.stack = []
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.my_win = False
        self.me_first = False
        self.my_turn = False
        self.game_over = False

    def select_player(self):
        players = ['@', '#', 'X', '&', 'O']
        self.player = input("select your player: ")[0]
        if self.player in players:
            players.remove(self.player)
        self.me = random.choice(players)

    def print_board(self):
        print("""
         {}  | {}  | {} 
        ____|____|____
            |    |
         {}  | {}  | {} 
        ____|____|____
            |    |
         {}  | {}  | {} 
            |    |   
        """.format(*self.board))

    def get_legal_options(self):
        options = [str(option) for option in range(1, 10)]
        return list(set(options).difference(self.stack))

    def my_move(self):
        print('my turn:')
        move = random.choice(self.get_legal_options())
        self.board[int(move)-1] = self.me
        self.stack.append(move)
        self.my_turn = False

    def player_move(self):
        move = False
        while not move:
            move = input('your turn: ')
            if move not in self.get_legal_options():
                move = False
                print('invalid move. try again please: ')
            else:
                self.board[int(move)-1] = self.player
                self.stack.append(move)
                self.my_turn = True

    def select_first(self):
        self.me_first = random.choice([True,False])
        if self.me_first:
            print('im the first to go')
            self.my_turn = True
        else:
            print('you go first')

    def set_game_over(self):
        combs = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]
        for comb in combs:
            if all(self.board[factor-1] == self.player for factor in comb):
                self.game_over = True
            elif all(self.board[factor-1] == self.me for factor in comb):
                self.game_over = True
                self.my_win = True

    def clear(self):
        self.player = None
        self.me = None
        self.stack = []
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.my_win = False
        self.me_first = False
        self.my_turn = False
        self.game_over = False

    def end_game(self):
        if self.my_win:
            print('GAME OVER!\n you are such a loser')
        else:
            print('YOU WON!')
        menu = input('to play again, press 0. press any other key to quit: ')
        if menu == '0':
            self.clear()
            self.play()
        else:
            if self.my_win:
                print('bye loser!!')
            else:
                print('bye bye!!')
            exit(0)

    def play(self):
        self.select_player()
        self.select_first()
        self.print_board()
        while not self.game_over:
            if self.my_turn:
                self.my_move()
            else:
                self.player_move()
            self.print_board()
            self.set_game_over()
        self.end_game()





