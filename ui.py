import sys
from wordle import WordleGame, WordleGuessError
from msvcrt import getch
from string import ascii_letters

class WordleUI:
    LETTERS = set(bytes(c, "ascii") for c in ascii_letters)
    COLORS = ["\x1b[39m", "\x1b[33m", "\x1b[32m"]
    def __init__(self) -> None:
        self.game = WordleGame()
        self.guesses = []
    
    def run(self) -> None:
        self.message = ""
        self.buffer = b""
        self.refresh()
        while self.game.playing:
            char = getch()
            # self.message = str(char)
            if char == b"\x03":
                sys.exit(1)
            if char == b"\x08":
                if self.buffer:
                    self.buffer = self.buffer[:-1]
            elif char == b"\r":
                self.guess()
            elif char in self.LETTERS:
                if len(self.buffer) < 5:
                    self.buffer += char
                    if self.message:
                        self.message = ""
            self.refresh()
    
    def guess(self) -> None:
        try:
            guess = str(self.buffer, "ascii")
            mark = self.game.guess(guess)
            colourised = "".join(self.COLORS[m] + l for m, l in zip(mark, guess)) + "\x1b[0m"
            self.guesses.append(colourised)
        except WordleGuessError:
            self.message = "invalid"
        self.buffer = b""
    
    def refresh(self) -> None:
        lines = []
        for i in range(self.game.max_guesses):
            if i < len(self.guesses):
                word = self.guesses[i]
            elif i == len(self.guesses):
                word = str(self.buffer, "ascii") + "_" * (5 - len(self.buffer)) # CAREFUL!
            else:
                word = "_____"
            lines.append(f"| {i+1} {word}   |")
        # print("\r" + str(self.buffer, "ascii"), end="")
        print(f"""\
+===========+
|  Wordle!  |
|  ({self.game.answer})   |
{'\n'.join(lines)}
|           |
|{self.message.center(11)}|
+===========+\x1b[{6+len(lines)}A""")
        print("\x1b[?25l", end="")

def main():
    WordleUI().run()

if __name__ == "__main__":
    main()