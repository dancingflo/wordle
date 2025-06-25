from wordle import WordleGame


def test_init_game():
    game = WordleGame()
    assert isinstance(game.answer, str)


def test_correct_guess():
    words = ["fungi", "hello", "flora", "fauna", "virus"]
    for word in words:
        game = WordleGame(answer=word)
        assert game.guess(word) == (2, 2, 2, 2, 2)
        
def test_max_guesses():
    game = WordleGame(answer="hello", max_guesses=5)
    for _ in range(5):
        game.guess("flora")
    assert game.playing == False
    assert game.completed == False
