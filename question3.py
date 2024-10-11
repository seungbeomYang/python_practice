class GameBoard:
    def __init__(self, size):
        self.size = size
        self.num_disks = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] * 2

    def num_free_positions_in_column(self, column):
        value = self.size
        for i in self.items[column]:
            if i != 0:
                value -= 1
        return value

    def game_over(self):
        for column in self.items:
            count1 = 0
            count2 = 0
            for character in column:
                if character == 1:
                    count1 += 1
                elif character == 2:
                    count2 += 1

            if count1 == self.size or count2 == self.size:
                return True
        count = 0
        for i in range(self.size):
            count1 = 0
            count2 = 0
            count += 1
            for column in range(len(self.items)):
                if self.items[column][self.size - count] == 1:
                    count1 += 1
                elif self.items[column][self.size - count] == 2:
                    count2 += 1

            if count1 == self.size or count2 == self.size:
                return True

        return False

    def display(self):
        count = 0
        for i in range(self.size):
            count += 1
            for column in range(len(self.items)):
                if self.items[column][self.size - count] == 1:
                    print("o", end=" ")
                elif self.items[column][self.size - count] == 2:
                    print("x", end=" ")
                else:
                    print("", end="  ")
                # for character in column:
                #     print(character, end=" ")
            print("")
        print('-', end="")
        for count in range(self.size - 1):
            print("--", end="")
        print("")
        for count in range(self.size):
            print(count, end=" ")
        print("")
        print(f"Points player 1: {self.points[0]}")
        print(f"Points player 2: {self.points[1]}")

    def num_new_points(self, column, row, player):
        point = 0
        touching = False
        for col in range(len(self.items)):
            count1 = 0
            count2 = 0
            for ro in range(len(self.items[col])):
                try:
                    if self.items[col][ro] == 1:
                        if self.items[col][ro] == self.items[col][ro + 1] and self.items[col][ro] == self.items[col][ro + 2] and self.items[col][ro] == self.items[col][ro + 3]:
                            self.points[0] += 1
                            if player == 1:
                                if column == col:
                                    if row == ro or row == ro + 1 or row == ro + 2 or row == ro+3:
                                        point += 1

                    elif self.items[col][ro] == 2:
                        if self.items[col][ro] == self.items[col][ro + 1] and self.items[col][ro] == self.items[col][ro + 2] and self.items[col][ro] == self.items[col][ro + 3]:
                            self.points[1] += 1
                            if player == 2:
                                if column == col:
                                    if row == ro or row == ro + 1 or row == ro + 2 or row == ro+3:
                                        point += 1

                except IndexError:
                    pass
        touching = False
        count = 0
        for i in range(self.size):
            count1 = 0
            count2 = 0
            count += 1
            for col in range(len(self.items)):
                try:
                    if self.items[col][self.size - count] == 1:
                        if self.items[col][self.size - count] == self.items[col + 1][self.size - count] and self.items[col][self.size - count] == self.items[col + 2][self.size - count] and self.items[col][self.size - count] == self.items[col + 3][self.size - count]:
                            self.points[0] += 1
                            if player == 1:
                                if column == col or column == col + 1 or column == col + 2 or column == col + 3:
                                    if row == self.size - count:
                                        point += 1

                    elif self.items[col][self.size - count] == 2:
                        if self.items[col][self.size - count] == self.items[col + 1][self.size - count] and self.items[col][self.size - count] == self.items[col + 2][self.size - count] and self.items[col][self.size - count] == self.items[col + 3][self.size - count]:
                            self.points[1] += 1
                            if player == 2:
                                if column == col or column == col + 1 or column == col + 2 or column == col + 3:
                                    if row == self.size - count:
                                        point += 1

                except IndexError:
                    pass
        for col in range(len(self.items)):
            for ro in range(len(self.items[col])):
                try:
                    if self.items[col][ro] == 1:

                        if self.items[col][ro] == self.items[col + 1][ro + 1] and self.items[col][ro] == self.items[col + 2][ro + 2] and self.items[col][ro] == self.items[col + 3][ro + 3]:
                            self.points[0] += 1
                            if player == 1:
                                if (column, row) == (col, ro) or (column, row) == (col + 1, ro + 1) or (column, row) == (col + 2, ro + 2) or (column, row) == (col + 3, ro + 3):
                                    point += 1

                    if self.items[col][ro] == 2:
                        if self.items[col][ro] == self.items[col + 1][ro + 1] and self.items[col][ro] == self.items[col + 2][ro + 2] and self.items[col][ro] == self.items[col + 3][ro + 3]:
                            self.points[1] += 1
                            if player == 2:
                                if (column, row) == (col, ro) or (column, row) == (col + 1, ro + 1) or (column, row) == (col + 2, ro + 2) or (column, row) == (col + 3, ro + 3):
                                    point += 1

                except IndexError:
                    pass
        for col in range(len(self.items)):
            for ro in range(len(self.items[col])):
                try:
                    if self.items[col][ro] == 2:
                        if self.items[col][ro] == self.items[col + 1][ro - 1] and self.items[col][ro] == self.items[col + 2][ro - 2] and self.items[col][ro] == self.items[col + 3][ro - 3]:
                            self.points[1] += 1
                            if player == 2:
                                if (column, row) == (col, ro) or (column, row) == (col + 1, ro - 1) or (column, row) == (col + 2, ro - 2) or (column, row) == (col + 3, ro - 3):
                                    point += 1

                    if self.items[col][ro] == 1:
                        if self.items[col][ro] == self.items[col + 1][ro - 1] and self.items[col][ro] == self.items[col + 2][ro - 2] and self.items[col][ro] == self.items[col + 3][ro - 3]:
                            self.points[0] += 1
                            if player == 1:
                                if (column, row) == (col, ro) or (column, row) == (col + 1, ro - 1) or (column, row) == (col + 2, ro - 2) or (column, row) == (col + 3, ro - 3):
                                    point += 1

                except IndexError:
                    pass
        return point

    def add(self, column, player):
        row = 0
        new_list = []
        for i in range(len(self.items[column])):
            if self.items[column][i] == 0:
                row = i
                board.items[column][row] = player
                break

        for i in range(len(self.items[column])):
            count = 0
            for character in self.items[i]:
                if character != 0:
                    count += 1

            new_list.append(count)

        self.num_disks = new_list


board = GameBoard(6)
board.add(2, 1)
board.add(3, 2)
board.add(3, 1)
board.add(2, 2)
board.add(4, 1)
board.add(1, 2)
board.add(2, 1)
board.add(3, 2)
board.add(0, 1)
board.add(4, 2)
board.add(3, 1)
board.add(4, 2)
board.add(5, 1)
board.add(4, 2)
board.add(4, 1)
board.add(2, 2)
board.add(1, 1)
board.add(1, 2)
board.add(1, 1)
board.add(1, 2)
board.add(1, 1)
board.add(0, 2)
board.add(0, 1)
board.add(0, 2)
board.add(0, 1)
board.add(0, 2)
print("Newly created 4-in-a-row sequences: ", board.num_new_points(0, 5, 2))
board.display()
