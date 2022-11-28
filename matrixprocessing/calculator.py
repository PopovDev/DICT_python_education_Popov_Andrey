"""Matrix calculator"""
from matrix import Matrix


class Calculator:
    """Matrix calculator"""

    def main_menu(self) -> int:
        """Main menu printing and input"""
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")

        while True:
            try:
                choice = int(input("Your choice: >"))
                if choice not in range(7):
                    raise ValueError
                return choice
            except ValueError:
                print("Invalid choice")

    def read_matrix(self) -> Matrix:
        """Read matrix from input"""
        while True:
            try:
                rows, coloumns = map(int, input(
                    "Enter size of matrix: >").split())
                if rows <= 0 or coloumns <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid size")
        print("Enter matrix:")
        matrix_data = []
        for _ in range(rows):
            while True:
                try:
                    matrix_input = list(map(float, input().split()))
                    if len(matrix_input) != coloumns:
                        raise ValueError
                    matrix_data.append(matrix_input)
                    break
                except ValueError:
                    print("Invalid size")

        return Matrix((rows, coloumns), matrix_data)

    def read_value(self) -> int | float:
        """Read value from input"""
        while True:
            try:
                value = float(input("Enter constant: >"))
                return value
            except ValueError:
                print("Invalid value")

    def __caltulate_sum(self) -> None:
        """Calculate sum of two matrices"""
        print("Entering first matrix")
        matrix1 = self.read_matrix()
        print("Entering second matrix")
        matrix2 = self.read_matrix()
        print("The result is:")
        print(matrix1 + matrix2)

    def __caltulate_const_mult(self) -> None:
        """Calculate multiplication of matrix by constant"""
        print("Entering matrix")
        matrix = self.read_matrix()
        value = self.read_value()
        print("The result is:")
        print(matrix * value)

    def __caltulate_mult(self) -> None:
        """Calculate multiplication of two matrices"""
        print("Entering first matrix")
        matrix1 = self.read_matrix()
        print("Entering second matrix")
        matrix2 = self.read_matrix()
        print("The result is:")
        print(matrix1 @ matrix2)

    def __calculate_transpose(self) -> None:
        """Calculate transpose of matrix"""
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        while True:
            try:
                choice = int(input("Your choice: >"))
                if choice not in range(1, 5):
                    raise ValueError
                break
            except ValueError:
                print("Invalid choice")
        print("Entering matrix")
        matrix = self.read_matrix()
        print("The result is:")
        match choice:
            case 1:
                print(matrix.transposed)
            case 2:
                print(matrix.transposed_sd)
            case 3:
                print(matrix.transposed_vertical)
            case 4:
                print(matrix.transposed_horizontal)

    def __calculate_determinant(self) -> None:
        """Calculate determinant of matrix"""
        print("Entering matrix")
        matrix = self.read_matrix()
        print("The result is:")
        print(matrix.determinant)

    def __calculate_inverse(self) -> None:
        """Calculate inverse of matrix"""
        print("Entering matrix")
        matrix = self.read_matrix()
        print("The result is:")
        print(matrix.inverse)

    def caltulator_loop(self) -> None:
        """Calculator loop"""
        while True:
            print()
            menu_choice = self.main_menu()
            print()
            try:
                match menu_choice:
                    case 1:
                        self.__caltulate_sum()
                    case 2:
                        self.__caltulate_const_mult()
                    case 3:
                        self.__caltulate_mult()
                    case 4:
                        self.__calculate_transpose()
                    case 5:
                        self.__calculate_determinant()
                    case 6:
                        self.__calculate_inverse()
                    case 0:
                        break
            except ValueError as err:
                print("!> Can't calculate:", err)
