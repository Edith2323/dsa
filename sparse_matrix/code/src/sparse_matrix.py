class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        if matrixFilePath:
            self.load_from_file(matrixFilePath)
        else:
            self.num_rows = numRows
            self.num_cols = numCols
            self.data = {}

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
               
                lines = [line.strip() for line in lines if line.strip()]
               
                self.num_rows = int(lines[0].split('=')[1])
                self.num_cols = int(lines[1].split('=')[1])
                self.data = {}
               
                for line in lines[2:]:
                    if line.startswith('(') and line.endswith(')'):
                        row, col, value = map(int, line[1:-1].split(','))
                        self.data[(row, col)] = value
                    else:
                        raise ValueError("Input file has wrong format")
        
        except Exception as e:
            raise ValueError(f"Error loading matrix: {str(e)}")

    def get_element(self, currRow, currCol):
        return self.data.get((currRow, currCol), 0)

    def set_element(self, currRow, currCol, value):
        self.data[(currRow, currCol)] = value

    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for addition")
        result = SparseMatrix(numRows=self.num_rows, numCols=self.num_cols)
        for (row, col), value in self.data.items():
            result.set_element(row, col, value + other.get_element(row, col))
        return result

    def subtract(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for subtraction")
        result = SparseMatrix(numRows=self.num_rows, numCols=self.num_cols)
        for (row, col), value in self.data.items():
            result.set_element(row, col, value - other.get_element(row, col))
        return result

    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions do not match for multiplication")
        result = SparseMatrix(numRows=self.num_rows, numCols=other.num_cols)
        for (row1, col1), value1 in self.data.items():
            for (row2, col2), value2 in other.data.items():
                if col1 == row2:
                    result.set_element(row1, col2, result.get_element(row1, col2) + value1 * value2)
        return result

    def __str__(self):
        output = f"rows={self.num_rows}\ncols={self.num_cols}\n"
        for (row, col), value in self.data.items():
            output += f"({row}, {col}, {value})\n"
        return output
