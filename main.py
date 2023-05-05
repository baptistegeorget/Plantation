from text_to_matrix import TextToMatrix
from algorithm import Algorithm

FILE = "tree.txt"


def main():
    matrix = TextToMatrix(FILE).get_matrix()
    algorithm = Algorithm(matrix)


if __name__ == "__main__":
    main()
