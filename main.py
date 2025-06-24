from wordle import WordleGame


def main():
    print("Welcome to Wordle!")
    game = WordleGame()
    while game.playing:
        guess = input()
        mark = game.guess(guess)
        print(mark)

main()