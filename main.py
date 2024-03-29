from text_to_matrix import TextToMatrix
from algorithm import Algorithm
import random

FILE = "tree.txt"
MATRIX_TEST = [
    [48, 25, 22],
    [35, 3, 35],
    [9, 28, 2],
    [29, 38, 1]
]


def generate_random_matrix(rows, cols, min_value, max_value):
    matrix = []
    for _ in range(rows):
        row = [random.randint(min_value, max_value) for _ in range(cols)]
        matrix.append(row)
    return matrix


def main():
    random_matrix = generate_random_matrix(100, 100, 55, 99)
    matrix = TextToMatrix(FILE).get_matrix()

    print("\nAlgorithme \"Glouton\" :")
    print(Algorithm(matrix).gluttonous())
    print("\nAlgorithme \"Récursif naïf\" :")
    print(Algorithm(matrix).naive())
    print("\nAlgorithme \"Top down\" :")
    print(Algorithm(matrix).top_down())
    print("\nAlgorithme \"Bottom up\" :")
    print(Algorithm(matrix).bottom_up())


if __name__ == "__main__":
    main()
