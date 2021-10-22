import pytest
import game


class TestGame:
    """
    TestGame
    """

    def test_show_board(self):
        """
        show_board
        """
    def test_one_step(self):
        """
        one_step
        """
        game_test = game.TicTacGame()
        game_test.one_step(1)
        assert game_test.map[0] == 'X'
        game_test.one_step(2)
        assert game_test.map[0] == '0'
        game_test.one_step(1)
        assert game.CellException


    def test_start_game(self):
        """
        start_game
        """

    def test_check_winner(self):
        """
        combinations
        """
if __name__ == '__main__':
    game = 
    game.start_game()