class Algorithm:

    __matrix = None

    def __init__(self, matrix):
        self.__matrix = matrix

    def gluttonous(self):
        list_of_species = []
        total_cost = 0
        last_column = -1
        for i in range(len(self.__matrix)):
            cost = float('inf')
            actual_column = -1
            for j in range(len(self.__matrix[i])):
                if last_column != j and cost > self.__matrix[i][j]:
                    actual_column = j
                    cost = self.__matrix[i][j]
            last_column = actual_column
            total_cost += cost
            list_of_species.append(cost)
        return total_cost, list_of_species

    def naive(self):
        pass

    def top_down(self):
        pass

    def bottom_up(self):
        pass
