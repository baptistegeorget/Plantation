class TextToMatrix:

    __name_file = None

    def __init__(self, name_file):
        self._name_file = name_file

    def __get_content(self):
        with open(self._name_file) as f:
            content = f.read()
            return content

    def get_matrix(self):
        content = self.__get_content()
        matrix = [[]]
        x = 0
        i = 0
        value = ""
        while i < len(content):
            if content[i] != " " and content[i] != "\n":
                value += content[i]
                i += 1
            elif content[i] != "\n":
                matrix[x].append(int(value))
                value = ""
                i += 1
            else:
                matrix[x].append(int(value))
                value = ""
                x += 1
                i += 1
                matrix.append([])
        matrix.pop(-1)
        return matrix
