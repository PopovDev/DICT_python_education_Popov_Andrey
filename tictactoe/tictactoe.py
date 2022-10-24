"""Tiktactoe game by Popov Andrey"""
from enum import Enum


class CellState(Enum):
    """Enum of cell states"""
    EMPTY = 0
    X = 1
    O = 2


class GameState(Enum):
    """Enum of game states"""
    X_MOVE = 0
    O_MOVE = 1
    X_WIN = 2
    O_WIN = 3
    DRAW = 4

    def __str__(self) -> str:
        """Return string representation of game state"""
        match self:
            case GameState.X_MOVE:
                return 'X Move'
            case GameState.O_MOVE:
                return 'O Move'
            case GameState.X_WIN:
                return 'X Wins'
            case GameState.O_WIN:
                return 'O Wins'
            case GameState.DRAW:
                return 'Draw'
        return 'Unknown'


class TicTacToe:
    """TicTacToe game representation class"""

    def __init__(self):
        """Initialize game"""
        self.state = [[CellState.EMPTY for _ in range(3)] for _ in range(3)]
        self.game_state = GameState.X_MOVE

    def check_rows(self):
        """Find winner in rows"""
        for row in self.state:
            if set(row) == {CellState.X}:
                return GameState.X_WIN
            if set(row) == {CellState.O}:
                return GameState.O_WIN
        return None

    def check_column(self):
        """Find winner in columns"""
        for i in range(3):
            column_set = {self.state[0][i], self.state[1][i], self.state[2][i]}
            if column_set == {CellState.X}:
                return GameState.X_WIN
            if column_set == {CellState.O}:
                return GameState.O_WIN
        return None

    def check_diagonals(self):
        """Find winner in diagonals"""
        diagonal_sets = [
            {self.state[0][0], self.state[1][1], self.state[2][2]},
            {self.state[0][2], self.state[1][1], self.state[2][0]},
        ]
        for diagonal_set in diagonal_sets:
            if diagonal_set == {CellState.X}:
                return GameState.X_WIN
            if diagonal_set == {CellState.O}:
                return GameState.O_WIN
        return None

    def calculate_game_state(self):
        """Find winner in game or draw"""

        if row_state := self.check_rows():
            self.game_state = row_state
        elif column_state := self.check_column():
            self.game_state = column_state
        elif diagonal_state := self.check_diagonals():
            self.game_state = diagonal_state
        else:
            for row in self.state:
                if CellState.EMPTY in row:
                    break
            else:
                self.game_state = GameState.DRAW

    def move(self, cord_x: int, cord_y: int):
        """Put X or O in cell if it is possible"""
        ocupated_cell_error = 'This cell is occupied! Choose another one!'
        if self.game_state == GameState.X_MOVE:
            if self.state[cord_x][cord_y] == CellState.EMPTY:
                self.state[cord_x][cord_y] = CellState.X
                self.game_state = GameState.O_MOVE
            else:
                print(ocupated_cell_error)
        elif self.game_state == GameState.O_MOVE:
            if self.state[cord_x][cord_y] == CellState.EMPTY:
                self.state[cord_x][cord_y] = CellState.O
                self.game_state = GameState.X_MOVE
            else:
                print(ocupated_cell_error)
        else:
            raise Exception('Game is over!')

    def print_table(self):
        """Print game table"""
        print('█████')
        for row in self.state:
            print('█', end='')
            for cell in row:
                match cell:
                    case CellState.EMPTY:
                        print(' ', end='')
                    case CellState.X:
                        print('X', end='')
                    case CellState.O:
                        print('O', end='')
            print('█')
        print('█████')


def game_loop():
    """Game loop function"""
    game = TicTacToe()

    while True:
        game.print_table()

        prompt_str = f'Enter the coordinates: {game.game_state}> '
        while True:
            try:
                cord_x, cord_y = input(prompt_str).split()
                cord_x, cord_y = int(cord_x), int(cord_y)
                if not 1 <= cord_x <= 3 or not 1 <= cord_y <= 3:
                    raise IndexError
                break
            except ValueError:
                print('You should enter numbers!')
            except IndexError:
                print('Coordinates should be from 1 to 3!')

        game.move(cord_x - 1, cord_y - 1)
        game.calculate_game_state()

        if game.game_state in [GameState.X_WIN, GameState.O_WIN, GameState.DRAW]:
            game.print_table()
            print(game.game_state)
            break


def main():
    """Main function"""
    try:
        while True:
            print('Print "start" to start game or "exit" to exit')
            command = input('> ')
            if command.lower() == 'start':
                try:
                    game_loop()
                except KeyboardInterrupt:
                    print('\nGame interrupted!')
            elif command.lower() == 'exit':
                break
            else:
                print('Unknown command')
    except KeyboardInterrupt:
        print('\nExiting...')

    print('Bye!')


if __name__ == "__main__":
    main()
