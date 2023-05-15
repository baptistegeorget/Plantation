class Algorithm:

    __matrix = None

    def __init__(self, matrix):
        self.__matrix = matrix

    def __min(self, list_elements, exclude_column):
        """
        :param list_elements: Liste d'entiers.
        :param exclude_column: Entier qui correspond à un emplacement à exclure dans la liste.
        :return: La valeur minimum et sa position dans la liste.
        """
        column = -1
        min_value = float('inf')
        for i in range(len(list_elements)):
            if i != exclude_column and list_elements[i] < min_value:
                column = i
                min_value = list_elements[i]
        return int(min_value), column

    def gluttonous(self):
        """
        :return: Le coût total de la plantation et la liste des essences utilisées dans l'ordre des emplacements.
        """
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
        """
        :return: Le coût total de la plantation.
        """
        total_cost, column = self.__naive_recursion(len(self.__matrix) - 1)
        return total_cost

    def __naive_recursion(self, i):
        """
        :param i: Emplacement actuel.
        :return: Le coût total et l'essence utilisée.
        """
        if i == 0:
            return self.__min(self.__matrix[i], -1)
        min_value1, column1 = self.__naive_recursion(i - 1)
        min_value2, column2 = self.__min(self.__matrix[i], column1)
        return min_value1 + min_value2, column2

    def top_down(self):
        """
        :return: Le coût total de la plantation.
        """
        memo = {}
        total_cost, column = self.__top_down_recursion(len(self.__matrix) - 1, memo)
        return total_cost

    def __top_down_recursion(self, i, memo):
        """
        :param i: Emplacement actuel.
        :param memo: Dictionnaire pour la mémoïsation des résultats précédents.
        :return: Le coût total et l'essence utilisée.
        """
        if i == 0:
            return self.__min(self.__matrix[i], -1)
        if i in memo:
            return memo[i]
        min_value1, column1 = self.__top_down_recursion(i - 1, memo)
        min_value2, column2 = self.__min(self.__matrix[i], column1)
        total_cost = min_value1 + min_value2
        memo[i] = total_cost, column2
        return total_cost, column2

    def bottom_up(self):
        """ 
        :return: Le coût total de la plantation.
        """############################################################## A FINIR
        n = len(self.__matrix)
        memo = {}
        memo[0] = (self.__min(self.__matrix[0], -1), -1)
        for i in range(1, n):
            min_value, column = self.__min(self.__matrix[i], memo[i - 1][1])
            total_cost = memo[i - 1][0] + min_value
            memo[i] = (total_cost, column)
        return memo[n - 1][0]
