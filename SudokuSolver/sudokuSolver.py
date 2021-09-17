from pprint import pprint

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]== -1:
                return r,c
    return None, None #if no empty and the puzzle is done
#finds the next empty row or col (which represented with -1), returns NONE NONE if there is none
#

def is_valid(puzzle, guess, row, col):
    row_values = puzzle[row]
    if guess in row_values:
        return False
    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False

    row_started = (row // 3) * 3
    col_started = (col // 3) * 3
    for r in range(row_started, row_started+3):
        for c in range(col_started, col_started+3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):#solves sudoku with backtracking
    row, col = find_next_empty(puzzle)
    #our sudoku is list of lists, we need to return if the puzzle is solvable
    if row is None:
        return True
    # if there is a space free then make a guess what number to put there
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)




