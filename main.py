from text_to_matrix import TextToMatrix
from algorithm import Algorithm

FILE = "tree.txt"
MATRIX_TEST = [
    [48, 25, 22],
    [35, 3, 35],
    [9, 28, 2],
    [29, 38, 1]
]


def main():
    matrix = TextToMatrix(FILE).get_matrix()
    algorithm = Algorithm(MATRIX_TEST)
    print(algorithm.gluttonous())


if __name__ == "__main__":
    main()
