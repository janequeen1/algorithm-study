def fill_right(matrix, start_value, cycle, size):
    value = start_value
    # Fill the top row from left to right
    for j in range(cycle, size - (cycle + 1)):
        matrix[cycle][j] = value
        value += 1
    return value

def fill_down(matrix, start_value, cycle, size):
    value = start_value
    # Fill the right column from top to bottom
    for i in range(cycle, size - (cycle + 1)):
        matrix[i][size - (cycle + 1)] = value
        value += 1
    return value

def fill_left(matrix, start_value, cycle, size):
    value = start_value
    # Fill the bottom row from right to left
    for j in range(size - (cycle + 1), cycle, -1):
        matrix[size - (cycle + 1)][j] = value
        value += 1
    return value

def fill_up(matrix, start_value, cycle, size):
    value = start_value
    # Fill the left column from bottom to top
    for i in range(size - (cycle + 2), cycle - 1, -1):
        matrix[i + 1][cycle] = value
        value += 1
    return value

def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    current_value = 1
    num_cycles = (n + 1) // 2

    for cycle in range(num_cycles):
        # Fill in the current cycle layer by layer
        current_value = fill_right(matrix, current_value, cycle, n)
        current_value = fill_down(matrix, current_value, cycle, n)
        current_value = fill_left(matrix, current_value, cycle, n)
        current_value = fill_up(matrix, current_value, cycle, n)

    # If n is odd, set the center value
    if n % 2 == 1:
        center = n // 2
        matrix[center][center] = current_value
    return matrix

def print_matrix(matrix):
    # Calculate the maximum width needed for formatting
    max_num = max(max(row) for row in matrix)
    max_width = len(str(max_num))
    # Print the matrix with proper formatting
    for row in matrix:
        print(' '.join(f'{num:{max_width}d}' for num in row))