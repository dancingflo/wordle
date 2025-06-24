from wordle import WordleGame, WordleGuessError

COLORS = ["\x1b[39m", "\x1b[33m", "\x1b[32m"]

def main():
    print("Welcome to Wordle!")
    game = WordleGame()
    while game.playing:
        guess = input()
        try:
            mark = game.guess(guess)
            print("\x1b[A\r"+ "".join(COLORS[m]+l for m, l in zip(mark, guess)) +"\x1b[0m")
        except WordleGuessError:
            print("\x1b[A\r      (invalid)\r\x1b[A")
        
main()