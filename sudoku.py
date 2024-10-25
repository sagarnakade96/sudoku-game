def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def take_inputs():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    
    while True:
        try:
            print_grid(grid)
            row = int(input("Enter the row (0-8) or -1 to stop: "))
            if row == -1:
                break
            col = int(input("Enter the column (0-8): "))
            num = int(input("Enter the number (1-9): "))
            if grid[row][col] == 0:
                grid[row][col] = num
            else:
                print("This position is already filled!")
        except ValueError:
            print("Invalid input, please enter valid numbers.")
    
    return grid

def is_valid(grid, row, col, num):
    # Check if the number is in the row
    if num in grid[row]:
        return False

    # Check if the number is in the column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check if the number is in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def main():
    print("Enter the known values for the Sudoku puzzle:")
    grid = take_inputs()
    
    if solve_sudoku(grid):
        print("Solved Sudoku:")
        print_grid(grid)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
