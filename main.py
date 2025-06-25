from wordle import WordleGame, WordleGuessError

COLORS = ["\x1b[39m", "\x1b[33m", "\x1b[32m"]

def main():
    print("Welcome to Wordle!")
    game = WordleGame()
    guesses = 0
    print(game.answer)
    while game.playing:
        guess = input()
        try:
            mark = game.guess(guess)
            print("\x1b[A\r"+ "".join(COLORS[m]+l for m, l in zip(mark, guess)) +"\x1b[0m")
            guesses += 1
            if mark == (2,2,2,2,2):
                print("Well Done!")
                break
            elif guesses == 6:
                print("Better luck next time. The word was", game.answer)
                break
        except WordleGuessError:
            print("\x1b[A\r      (invalid)\r\x1b[A")
     
        
main()