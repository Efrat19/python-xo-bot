from xo import Xo


def chat():
    while True:
        print('bla bla bla')


def quit_():
    print('bye!')
    quit()


def menu():
    answer = input("what do you wana do? ")
    words = answer.split(' ')
    options = ["play", "chat", "quit"]
    for option in options:
        if option in words:
            return option
    print('sorry, its beyond my abilities...')
    return False


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


if __name__ == '__main__':
    main()


