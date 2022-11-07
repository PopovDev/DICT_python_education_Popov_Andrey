"""Task Matrix processing module"""


class Matrix:
    """Implements a matrix class"""

    def __init__(self, size: tuple[int, int], matrix: list[list[int | float]]):
        self.size = size
        self.matrix = matrix
        if size[0] != len(matrix) or size[1] != len(matrix[0]):
            raise ValueError("Invalid matrix size")

    def __getitem__(self, key: tuple[int, int]) -> int | float:
        """Get item from matrix"""
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: int | float):
        """Set item in matrix"""
        self.matrix[key[0]][key[1]] = value

    @property
    def c_rows(self) -> int:
        """Number of rows"""
        return self.size[0]

    @property
    def c_coloumns(self) -> int:
        """Number of coloumns"""
        return self.size[1]

    @property
    def is_square(self) -> bool:
        """Is matrix square"""
        return self.c_rows == self.c_coloumns

    @staticmethod
    def zero(size: tuple[int, int]):
        """Generate zero matrix with given size"""
        matrix = []
        for _ in range(size[0]):
            matrix.append([0] * size[1])
        return Matrix(size, matrix)

    def __str__(self) -> str:
        """String representation of matrix"""
        strs = []
        strs.append(f"Matrix {self.size[0]}x{self.size[1]}")
        for row in self.matrix:
            col_strs = []
            for item in row:
                str_v = str(item)
                if str_v.endswith(".0"):
                    str_v = str_v[:-2]
                else:
                    str_v = str(round(item, 2))
                col_strs.append(str_v)
            strs.append(" ".join(col_strs))
        return "\n".join(strs)

    def __add__(self, other):
        """Addition of matrices"""
        if not isinstance(other, Matrix):
            raise TypeError("Not a matrix")
        if self.size != other.size:
            raise ValueError("Matrix must be the same size")
        new_matrix = Matrix.zero(self.size)
        for i in range(self.c_rows):
            for j in range(self.c_coloumns):
                new_matrix[i, j] = self[i, j] + other[i, j]
        return new_matrix

    def __mul__(self, other: int | float):
        """Multiplication of matrix by number"""
        new_matrix = Matrix.zero(self.size)
        for i in range(self.c_rows):
            for j in range(self.c_coloumns):
                new_matrix[i, j] = other * self[i, j]
        return new_matrix

    def __rmul__(self, other: int | float):
        """Multiplication of matrix by number"""
        return self * other

    def __matmul__(self, other):
        """Matrix multiplication"""
        if not isinstance(other, Matrix):
            raise TypeError("Not a matrix")
        if self.c_rows != other.c_coloumns:
            raise ValueError("Matrix has invalid size for multiplication")
        new_matrix = Matrix.zero((self.c_rows, other.c_coloumns))

        for i in range(self.c_rows):
            for j in range(other.c_coloumns):
                for k in range(self.c_coloumns):
                    new_matrix[i, j] += self[i, k] * other[k, j]
        return new_matrix

    @property
    def transposed(self):
        """Transpose of matrix - main diagonal"""
        new_matrix = Matrix.zero((self.c_coloumns, self.c_rows))
        for i in range(self.c_rows):
            for j in range(self.c_coloumns):
                new_matrix[j, i] = self[i, j]
        return new_matrix

    @property
    def transposed_sd(self):
        """Transpose of matrix - second diagonal"""
        new_matrix = Matrix.zero((self.c_coloumns, self.c_rows))
        for i in range(self.c_rows):
            for j in range(self.c_coloumns):
                new_matrix[j, i] = self[self.c_rows - i - 1, self.c_coloumns - j - 1]
        return new_matrix

    @property
    def transposed_vertical(self):
        """Transpose of matrix - vertical lines"""
        new_matrix = Matrix.zero(self.size)
        for i in range(self.c_rows):
            for j in range(self.c_coloumns):
                new_matrix[i, j] = self[i, self.c_coloumns - j - 1]
        return new_matrix

    @property
    def transposed_horizontal(self):
        """Transpose of matrix - horizontal lines"""
        new_matrix = Matrix.zero(self.size)
        for i in range(self.c_rows):
            for j in range(self.c_coloumns):
                new_matrix[i, j] = self[self.c_rows - i - 1, j]
        return new_matrix

    def minor(self, row: int, coloumn: int):
        """Minor of matrix"""
        new_matrix = Matrix.zero((self.c_rows - 1, self.c_coloumns - 1))
        for i in range(self.c_rows):
            for j in range(self.c_coloumns):
                if i == row or j == coloumn:
                    continue
                new_matrix[i - int(i > row), j - int(j > coloumn)] = self[i, j]
        return new_matrix

    @property
    def determinant(self) -> int | float:
        """Find determinant of matrix"""
        if not self.is_square:
            raise ValueError("Matrix must be square")
        if self.c_rows == 1:
            return self[0, 0]
        if self.c_rows == 2:
            return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]
        det = 0
        for i in range(self.c_rows):
            sign = (-1) ** i
            multiplier = self[i, 0] * sign
            det += self.minor(i, 0).determinant * multiplier
        return det

    @property
    def inverse(self):
        """Inverse matrix of matrix"""
        det = self.determinant
        if det == 0:
            raise ValueError("Matrix has no inverse")
        if self.c_rows == 1:
            return Matrix((1, 1), [[1 / det]])
        new_matrix = Matrix.zero(self.size)
        for i in range(self.c_rows):
            for j in range(self.c_coloumns):
                sign = (-1) ** (i + j)
                adding = sign * self.transposed.minor(i, j).determinant
                new_matrix[i, j] = adding
        return new_matrix * (1 / det)
