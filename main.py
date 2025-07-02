import shutil
import sys
from wordle import WordleGame, WordleGuessError
from msvcrt import getch
from string import ascii_letters


class WordleUI:
    LETTERS = set(bytes(c, "ascii") for c in ascii_letters)
    COLORS = ["\x1b[39m", "\x1b[33m", "\x1b[32m"]
    MESSAGES = ["Magic!", "Genius!", "Amazing!", "Great!", "Solid!", "Phew!"]

    def __init__(self) -> None:
        self.game = WordleGame()
        self.guesses = []

    def run(self) -> None:
        # print(self.game.answer)
        size = shutil.get_terminal_size()
        if size.lines < self.game.max_guesses + 6 or size.columns < 11:
            print("Terminal smaller than (12, 11)")
            return
        self.message = ""
        self.buffer = b""
        self.refresh()
        while self.game.playing:
            char = getch()
            # self.message = str(char)
            if char == b"\x03":  # ctrl
                print("\x1b[11B", end="")
                sys.exit(1)
            if char == b"\x08":  # delete
                if self.buffer:
                    self.buffer = self.buffer[:-1]
            elif char == b"\r":  # enter
                self.guess()
            elif char in self.LETTERS:
                if len(self.buffer) < 5:
                    self.buffer += char
                    if self.message:
                        self.message = ""
            self.refresh()
        self.exit()

    def guess(self) -> None:
        try:
            guess = str(self.buffer, "ascii")
            mark = self.game.guess(guess)
            colourised = (
                "".join(self.COLORS[m] + l for m, l in zip(mark, guess)) + "\x1b[0m"
            )
            self.guesses.append(colourised)
        except WordleGuessError:
            self.message = "invalid"
        self.buffer = b""

    def exit(self) -> None:
        if self.game.completed:
            self.message = self.MESSAGES[self.game.guesses - 1]
        else:
            self.message = self.COLORS[2] + self.game.answer + "\x1b[0m"
        self.refresh()
        print("\x1b[11B", end="")

    def refresh(self) -> None:
        lines = []
        for i in range(self.game.max_guesses):
            if i < len(self.guesses):
                word = self.guesses[i]
            elif i == len(self.guesses) and self.game.playing:
                word = (
                    "\x1b[1m"
                    + str(self.buffer, "ascii")
                    + "_" * (5 - len(self.buffer))
                    + "\x1b[22m"
                )  # CAREFUL!
            else:
                word = "_____" if self.game.playing else "     "
            lines.append(f"| {i+1 if self.game.playing else ' '} {word}   |")
        # print("\r" + str(self.buffer, "ascii"), end="")
        print(
            f"""\
+===========+
|  \x1b[1mWordle!\x1b[22m  |
|           |
{'\n'.join(lines)}
|           |
|{self.message.center(11)}|
+===========+\x1b[{6+len(lines)}A"""
        )
        print("\x1b[?25l", end="")


# if self.game.playing else self.message
def main():
    WordleUI().run()


if __name__ == "__main__":
    main()
