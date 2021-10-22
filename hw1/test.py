import pytest
import game
"""************* Module test
test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test.py:10:4: R0201: Method could be a function (no-self-use)
test.py:29:4: R0201: Method could be a function (no-self-use)
test.py:45:4: R0201: Method could be a function (no-self-use)

-----------------------------------
Your code has been rated at 9.00/10
"""

class TestGame:
    """
    TestGame
    """

    def test_one_step(self):
        """
        one_step
        """
        game_test = game.TicTacGame(3)
        game_test.init_board()
        game_test.one_step(1)
        assert game_test.map[0][0] == 'X'
        game_test.one_step(2)
        assert game_test.map[0][1] == '0'
        with pytest.raises(game.CellException):
            game_test.one_step(1)
            game_test.one_step(-1)
            game_test.one_step(0)
            game_test.one_step('DDDDDD')
        game_test_zero = game.TicTacGame()
        with pytest.raises(ZeroDivisionError):
            game_test_zero.one_step(2)

    def test_check_winner(self):
        """
        combinations
        """
        game_test = game.TicTacGame(3)
        game_test.init_board()
        assert game_test.check_winner
        game_test.map = [['X', 'X', 'X'], ['0', 5, '0'], [7, 8, 9]]
        assert not game_test.check_winner
        game_test.map = [['x', 'X', 'X'], ['0', '0', '0'], [9, 'X', 11]]
        assert not game_test.check_winner
        game_test.map = [[1, 2, 3], ['0', 5, '0'], ['X', 'X', 'X']]
        assert not game_test.check_winner
        game_test.map = [['X', 2, 3], ['0', 'X', '0'], [7, '0', 'X']]
        assert not game_test.check_winner

    def test_init_board(self):
        """
        combinations
        """
        game_test = game.TicTacGame('HH')
        with pytest.raises(game.InitBoardException):
            game_test.init_board()
            game_test.size = 0
            game_test.init_board()
            game_test.size = 1
            game_test.init_board()
            game_test.size = 2
            game_test.init_board()
