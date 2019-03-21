from xo import Xo
import random


def chat():
    while True:
        print('bla bla bla')


def quit_():
    print('bye!')
    quit()


def menu():
    answer = input("what do you wana do? ")
    words = answer.split(' ')
    options = ["play", "chat", "quit","run"]
    for option in options:
        if option in words:
            return option
    print('sorry, its beyond my abilities...')
    return False


def play_alone(counter):
    bot1 = Xo()
    bot2 = Xo()
    is_1_first = random.choice([True,False])
    bot1.me_first = is_1_first
    bot2.me_first = not is_1_first
    bot1.me = 'X'
    bot1.player = 'O'
    bot2.me = 'O'
    bot2.player = 'X'
    while counter:
        bot1.clear()
        bot2.clear()
        while not bot1.game_over:
            if bot1.my_turn:
                bot1.my_move()
                bot2.stack = bot1.stack
            else:
                bot2.my_move()
                bot1.stack = bot2.stack
            bot1.set_game_over()
        if not bot1.is_standoff:
            bot1.save_stack()
            msg = 'bot1 won' if bot1.my_win else 'bot2 won'
            counter -= counter
        else:
            msg = 'standoff'
        print(msg)
    



def main():
    print("hi!!")
    selected = None
    while not selected:
        selected = menu()

    if selected == 'play':
        xo = Xo()
        xo.play()
    elif selected == 'chat':
        chat()
    elif selected == 'quit':
        quit_()
    elif selected == 'run':
        counter = input('how many times?')
        play_alone(int(counter))


if __name__ == '__main__':
    main()


