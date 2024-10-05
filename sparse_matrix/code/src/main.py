import os
from sparse_matrix import SparseMatrix

def save_output(matrix, operation, file1, file2):
    output_dir = os.path.join(os.path.dirname(__file__), '../outputs/')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{os.path.basename(file1).split('.')[0]}_{operation}_{os.path.basename(file2).split('.')[0]}.txt")
    with open(output_file, 'w') as f:
        f.write(str(matrix))
    print(f"Output saved to: {output_file}")

def main():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    
    choice = input("Enter choice (1/2/3): ")

    file1 = input("Enter the path for the first matrix file: ")
    file2 = input("Enter the path for the second matrix file: ")

    try:
        matrix1 = SparseMatrix(file1)
        matrix2 = SparseMatrix(file2)

        if choice == '1':
            result = matrix1.add(matrix2)
            save_output(result, "plus", file1, file2)
        elif choice == '2':
            result = matrix1.subtract(matrix2)
            save_output(result, "minus", file1, file2)
        elif choice == '3':
            result = matrix1.multiply(matrix2)
            save_output(result, "times", file1, file2)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
