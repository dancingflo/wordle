import random

class WordleGuessError(Exception):
    pass

class WordleGame:
    def __init__(self, answer=None, max_guesses=6) -> None:
        with open("data/guesses.txt") as f:
            self.valid_guesses = set(f.read().splitlines())
        if answer is None:
            with open("data/answers.txt") as f:
                pos_answers = f.read().splitlines()
            self.answer = random.choice(pos_answers)
        else:
            self.answer = answer
        self.playing = True
        self.guesses = 0
        self.max_guesses = max_guesses
        self.completed = False

    def guess(self, guess: str) -> tuple[int]:
        if guess not in self.valid_guesses:
            raise WordleGuessError(f"Guess '{guess}' not in word list")
        guess_letters = ""
        self.guesses += 1
        mark = [0, 0, 0, 0, 0]
        for i, letter in enumerate(guess):
            if letter == self.answer[i]:
                guess_letters += letter
                mark[i] = 2
            elif letter in self.answer:
                if self.answer.count(letter)> guess_letters.count(letter):
                    mark[i] = 1
                    guess_letters += letter
        mark = tuple(mark)
        if mark == (2, 2, 2, 2, 2):
            self.playing = False
            self.completed = True
        elif self.guesses >= self.max_guesses:
            self.playing = False
        return mark
