"""

Реализовать игру крестики нолики в виде класса
************* Module game
game.py:110:12: R1705: Unnecessary "elif" after "return" (no-else-return)

------------------------------------------------------------------
Your code has been rated at 9.87/10 (previous run: 9.73/10, +0.14)

"""
import sys


class CellException(Exception):
    """
    CellException
    """


class ExitException(Exception):
    """
    CellException
    """


class TicTacGame:
    """
        TicTacGame
    """

    def __init__(self, size=0):
        self.size = size
        self.map = []
        self.init_board()
        self.num_steps = 0

    def init_board(self):
        """
        init_board
        """
        cell = 0
        for _ in range(0, self.size):
            self.map.append([cell + i for i in range(1, self.size + 1)])
            cell += self.size

    def show_board(self):
        """
        show_board
        """
        max_len = max([len(str(e)) for r in self.map for e in r])
        for row in self.map:
            print(*list(map(f'{{:>{max_len}}}'.format, row)))

    def one_step(self, cell):
        """
        one_step
        """
        # поймать ошибку выхода из поля
        # ошибка повторного хода по заполненному полю
        if isinstance(self.map[(cell - 1) // self.size][(cell - 1) % self.size], str):
            raise CellException
        if self.num_steps % 2 == 0:
            self.map[(cell - 1) // self.size][(cell - 1) % self.size] = 'X'
        elif self.num_steps % 2 == 1:
            self.map[(cell - 1) // self.size][(cell - 1) % self.size] = '0'
        self.num_steps += 1

    def start_game(self):
        """
        start_game
        """
        print('Please enter size of desk')
        self.size = int(input())
        if self.size <= 1:
            sys.exit(f'Illegal size {self.size} of map in game\n')
        self.init_board()
        self.show_board()
        while self.check_winner:
            try:
                print("Please choose a cell or finish game by 'EXIT' ")
                cell = input()
                if (cell == 'EXIT') | (cell == 'exit'):
                    raise ExitException
                self.one_step(int(cell))
                self.show_board()
            except IndexError:
                sys.stderr.write('Out of map\n')
            except CellException:
                sys.stderr.write('The cell is wrong\n')
            except ExitException:
                sys.exit('The game is ended! No winners!\n')
        if self.num_steps % 2 == 1:
            print('The gamerX is a winner!')
        else:
            print('The gamer0 is a winner!')

    @property
    def check_winner(self):
        """
        combinations
        """
        if self.map:
            cell0 = ''
            cell1 = ''
            cell2 = ''
            cell_x1 = ''
            cell_x2 = ''
            counter = 0
            for i in self.map:
                result = ''
                cell0 += str(i[0])
                cell1 += str(i[1])
                cell2 += str(i[2])
                cell_x1 += str(i[0 + counter])
                cell_x2 += str(i[2 - counter])
                counter += 1
                for cell in i:
                    result += str(cell)
                if result == i[0] * len(i):
                    return False

            if (cell0 == cell0[0] * len(cell0)) | \
                    (cell1 == cell1[0] * len(cell1)) | \
                    (cell2 == cell2[0] * len(cell2)):
                return False

            elif (cell_x1 == cell_x1[0] * len(cell_x1)) | \
                    (cell_x2 == cell_x2[0] * len(cell_x1)):
                return False
        return True


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
