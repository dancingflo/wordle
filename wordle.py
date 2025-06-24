import random

class WordleGuessError(Exception):
    pass

class WordleGame:
    def __init__(self, answer=None) -> None:
        with open("data/guesses.txt") as f:
            self.valid_guesses = set(f.read().splitlines())
        if answer is None:
            with open("data/answers.txt") as f:
                pos_answers = f.read().splitlines()
            self.answer = random.choice(pos_answers)
        else:
            self.answer = answer
        self.playing = True

    def guess(self, guess: str) -> tuple[int]:
        if guess not in self.valid_guesses:
            raise WordleGuessError(f"Guess '{guess}' not in word list")
        mark = [0, 0, 0, 0, 0]
        for i, letter in enumerate(guess):
            if letter == self.answer[i]:
                mark[i] = 2
            elif letter in self.answer:
                mark[i] = 1
        return tuple(mark)