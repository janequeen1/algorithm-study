import spiral_matrix

if __name__ == "__main__":
    n = int(input("Please input n: "))
    spiral_matrix_generated = spiral_matrix.generate_spiral_matrix(n)
    spiral_matrix.print_matrix(spiral_matrix_generated)