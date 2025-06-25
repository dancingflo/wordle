import sys
from wordle import WordleGame
from msvcrt import getch
from string import ascii_letters

class WordleUI:
    LETTERS = set(bytes(c, "ascii") for c in ascii_letters)
    def __init__(self) -> None:
        self.game = WordleGame()
        self.guesses = []
    
    def run(self) -> None:
        self.buffer = b""
        self.refresh()
        while self.game.playing:
            char = getch()
            if char == b"\x03":
                sys.exit(1)
            if char == b"\x08":
                if self.buffer:
                    self.buffer = self.buffer[:-1]
            elif char in self.LETTERS:
                self.buffer += char
            self.refresh()
    
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
|           |
{'\n'.join(lines)}
|           |
| Message   |
+===========+""")

def main():
    WordleUI().run()

if __name__ == "__main__":
    main()