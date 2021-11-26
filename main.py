import numpy as np


class Game:
    def __init__(self, number, move):
        self.number = number
        self.move = move


    def wolf_move_forward_left(self):
        if j > 0 and A[i - 1, j - 1] == 0:
            A[i, j] = 0
            A[i - 1, j - 1] = 1
            print(A)

        else:
            print('Wrong direction')


    def wolf_move_forward_right(self):
        if j < 7 and A[i - 1, j + 1] == 0:
            A[i, j] = 0
            A[i - 1, j + 1] = 1
            print(A)

        else:
            print('Wrong direction')


    def wolf_move_backward_right(self):
        if j < 7 and A[i + 1, j + 1] == 0:
            A[i, j] = 0
            A[i + 1, j + 1] = 1
            print(A)

        else:
            print('Wrong direction')


    def wolf_move_backward_left(self):
        if j > 0 and A[i + 1, j - 1] == 0:
            A[i, j] = 0
            A[i + 1, j - 1] = 1
            print(A)

        else:
            print('Wrong direction')


    def sheep_move_left(self):
        if j < 7 and A[i + 1, j + 1] == 0:
            A[i, j] = 0
            A[i + 1, j + 1] = 2
            print(A)

        elif j < 6 and A[i + 1, j + 1] == 1:
            A[i, j] = 0
            A[i + 1, j + 1] = 0
            A[i + 2, j + 2] = 2
            print(A)

        else:
            print('Wrong direction')


    def sheep_move_right(self):
        if j > 0 and A[i + 1, j - 1] == 0:
            A[i, j] = 0
            A[i + 1, j - 1] = 2
            print(A)

        elif j > 1 and A[i + 1, j - 1] == 1:
            A[i, j] = 0
            A[i + 1, j - 1] = 0
            A[i + 2, j - 2] = 2
            print(A)

        else:
            print('Wrong direction')


    def wolf_cant_moves(self):
        coordinates = np.where(A == 1)
        k = coordinates[0]
        l = coordinates[1]
        if ((l > 0 and l < 7 ) and (A[k - 1, l - 1] == 2 and A[k + 1, l + 1] == 2 and A[k - 1, l + 1] == 2 and A[k + 1, l - 1] == 2)) \
                or (l == 0 and (A[k - 1, l + 1] and A[k + 1, l + 1]) == 2) or (l == 7 and (A[k - 1, l - 1] and A[k + 1, l - 1]) == 2):
            wolf_loses.append('wolf loses')
            print('Sheep wins')


    def moves(self):
        if self.number in y:
                if A[i, j] == 1:
                    if self.move == 'fl':
                        self.wolf_move_forward_left()
                        self.wolf_cant_moves()

                    elif self.move == 'fr':
                        self.wolf_move_forward_right()
                        self.wolf_cant_moves()

                    elif self.move == 'bl':
                        self.wolf_move_backward_left()
                        self.wolf_cant_moves()

                    elif self.move == 'br':
                        self.wolf_move_backward_right()
                        self.wolf_cant_moves()

                    else:
                        print('Wrong direction')

                elif A[i, j] == 2:
                    if self.move == 'l':
                        self.sheep_move_left()
                        self.wolf_cant_moves()


                    elif self.move == 'r':
                        self.sheep_move_right()
                        self.wolf_cant_moves()


                    else:
                        print('Wrong direction')


A = np.array([[0, 2, 0, 2, 0, 2, 0, 2],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0]])


B = np.array([['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
              ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
              ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
              ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
              ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
              ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
              ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
              ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']])


print(A)

wolf_loses = []

while not list(A[0]).count(1) and not wolf_loses:
    number, move = input("Enter a number of checker and move (l/r): ").split()
    game = Game(number=number, move=move)

    for i, x in enumerate(B):
        for j, y in enumerate(x):
            game.moves()