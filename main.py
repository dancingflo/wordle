from wordle import WordleGame, WordleGuessError

COLORS = ["\x1b[39m", "\x1b[33m", "\x1b[32m"]
MESSAGES = ["Magic!", "Genius!", "Amazing!", "Great!", "Solid!", "Phew!"]


def main():
    print("Welcome to Wordle!")
    game = WordleGame()
    while game.playing:
        guess = input()
        try:
            mark = game.guess(guess)
            print(
                "\x1b[A\r"
                + "".join(COLORS[m] + l for m, l in zip(mark, guess))
                + f"  {game.guesses}/{game.max_guesses}"
                + "\x1b[0m"
            )
        except WordleGuessError:
            print("\x1b[A\r      (invalid)\r\x1b[A")
    if game.completed:
        print(MESSAGES[game.guesses -1])
    else:
        print("Better luck next time. The word was", game.answer)


main()
