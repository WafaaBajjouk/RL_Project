import copy

class State:
    def __init__(self, size=3, c=None):
        self.size = size
        self.actions = ['front', 'back', 'left', 'right', 'top', 'bottom']
        if c:
            # 2D lists representing the six faces of the cube.
            self.d = c
            self.__front__ = c["front"]
            self.__back__ = c["back"]
            self.__left__ = c["left"]
            self.__right__ = c["right"]
            self.__top__ = c["top"]
            self.__bottom__ = c["bottom"]
            # list all sides of the cube.
            self.__sides__ = [self.front(), self.back(), self.left(), self.right(), self.top(), self.bottom()]
            return
        self.__front__ = [['W','W','W'],['W','W','W'],['W','W','W']]
        self.__back__ = [['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']]
        self.__top__ = [['R','R','R'],['R','R','R'],['R','R','R']]
        self.__bottom__ = [['O','O','O'],['O','O','O'],['O','O','O']]
        self.__left__ = [['B','B','B'],['B','B','B'],['B','B','B']]
        self.__right__ = [['G','G','G'],['G','G','G'],['G','G','G']]
        self.__sides__ = [self.front(), self.back(), self.left(), self.right(), self.top(), self.bottom()]
        #map the names of the sides to their corresponding 2D lists.
        self.d = {"front": self.front(), "back": self.back(), "left": self.left(),\
                    "right": self.right(), "top": self.top(), "bottom": self.bottom()} 

    def copy(self):
        return copy.deepcopy(self)

    def eq(self, other):
        return self.__left__ == other.left() and self.__right__ == other.right()\
                and self.__top__ == other.top() and self.__bottom__ == other.bottom()\
                and self.__front__ == other.front() and self.__back__ == other.back()

    def left(self):
        return self.__left__

    def set_left(self, l):
        self.__left__ = l

    def right(self):
        return self.__right__

    def set_right(self, r):
        self.__right__ = r

    def top(self):
        return self.__top__

    def set_top(self, t):
        self.__top__ = t

    def bottom(self):
        return self.__bottom__

    def set_bottom(self, b):
        self.__bottom__ = b

    def front(self):
        return self.__front__

    def set_front(self, f):
        self.__front__ = f

    def back(self):
        return self.__back__

    def set_back(self, b):
        self.__back__ = b

# gives a string repres of the cube's state.
    def __str__(self):
        return "\nFRONT" + str(self.__front__) + "\nBACK" + str(self.__back__) + "\nLEFT" \
        + str(self.__left__) + "\nRIGHT" + str(self.__right__) + "\nTOP" + str(self.__top__) + "\nBOTTOM" + str(self.__bottom__)

    def __hash__(self):
        return hash(self.__str__())

    def rotate_side(self, side):
        new_side = [[],[],[]]
        for i in reversed(range(self.size)):
            for y in range(self.size):
                new_side[self.size - 1 - i].append(side[i][self.size - 1 - y])
        return new_side

    def columns_to_rows(self, side, reverse=False):
        new_side = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if not reverse:
                    row.append(side[self.size - 1 - j][i])
                else:
                    row.append(side[j][self.size - 1 - i])
            new_side.append(row)
        return new_side

    def rotate_cube(self):
        left_side = self.__left__
        self.__left__ = self.replace_side(self.__back__)
        front_side = self.__front__
        self.__front__ = self.replace_side(left_side)
        right_side = self.__right__
        self.__right__ = self.replace_side(front_side)
        self.__back__ = self.replace_side(right_side)
        self.__top__ = self.columns_to_rows(self.__top__, reverse=True)
        self.__bottom__ = self.columns_to_rows(self.__bottom__)

    def swap_first_row(self, side1, side2):
        s1_1 = side1[0]
        s2_1 = side2[0]
        new_side1 = [s2_1] + list(side for side in side1[1:])
        new_side2 = [s1_1] + list(side for side in side2[1:])
        return new_side1, new_side2

    def swap_first_last_col(self, side1, side2):
        for i in range(len(side1)):
            side1[i][self.size - 1], side2[i][0] =  side2[i][0], side1[i][self.size - 1]
        return side1, side2

    def replace_side(self, side):
        new_side = []
        for row in side:
            new_side.append(row)
        return new_side

    def flip_forward(self):
        front = self.__front__
        self.__front__ = self.replace_side(self.__top__)
        bottom = self.__bottom__
        self.__bottom__ = self.replace_side(front)
        back = self.__back__
        self.__back__ = self.replace_side(bottom)
        self.__top__ = self.replace_side(back)

    def flip_backward(self):
        front = self.__front__
        self.__front__ = self.replace_side(self.__bottom__)
        top = self.__top__
        self.__top__ = self.replace_side(front)
        back = self.__back__
        self.__back__ = self.replace_side(top)
        self.__bottom__ = self.replace_side(back)

    def flip_cube(self, forward=False):
        if forward:
            self.flip_forward()
            self.__front__ = self.rotate_side(self.__front__)
            self.__back__ = self.rotate_side(self.__back__)
            self.__left__ = self.columns_to_rows(self.__left__)
            self.__right__ = self.columns_to_rows(self.__right__, reverse=True)
        else:
            self.flip_backward()
            self.__top__ = self.rotate_side(self.__top__)
            self.__bottom__ = self.rotate_side(self.__bottom__)
            self.__left__ = self.columns_to_rows(self.__left__, reverse=True)
            self.__right__ = self.columns_to_rows(self.__right__)

    def turn_front(self):
        self.__front__ = self.rotate_side(self.__front__)
        self.__top__, self.__bottom__ = self.swap_first_row(self.__top__, self.__bottom__)
        self.__left__, self.__right__ = self.swap_first_last_col(self.__left__, self.__right__)

    def turn_back(self):
        self.rotate_cube()
        self.rotate_cube()
        self.turn_front()
        self.rotate_cube()
        self.rotate_cube()

    def turn_left(self):
        self.rotate_cube()
        self.turn_front()
        self.rotate_cube()
        self.rotate_cube()
        self.rotate_cube()

    def turn_right(self):
        self.rotate_cube()
        self.rotate_cube()
        self.rotate_cube()
        self.turn_front()
        self.rotate_cube()

    def turn_top(self):
        self.flip_cube(forward=True)
        self.turn_front()
        self.flip_cube()

    def turn_bottom(self):
        self.flip_cube()
        self.turn_front()
        self.flip_cube(forward=True)


#   !!!! Checks if the cube is in the solved state by verifying that each face has the same color in all positions
    def isGoalState(self):
        for side in self.__sides__:
            char = side[0][0]
            for row in side:
                if not char == row[0] == row[1] == row[2]:
                    return False
        return True

# Executes a move based on the given action (left, right, front, back, top, bottom)   , to do : check for better implementations
    def move(self, action):
        if action == 'left':
            self.turn_left()
        elif action == 'right':
            self.turn_right()
        elif action == 'front':
            self.turn_front()
        elif action == 'back':
            self.turn_back()
        elif action == 'top':
            self.turn_top()
        elif action == 'bottom':
            self.turn_bottom()
        self.__sides__ = [self.front(), self.back(), self.left(), self.right(), self.top(), self.bottom()]


# Cube Manipulation Methods: 
# rotate_side: Rotates a given side of the cube clockwise.
# columns_to_rows: Converts columns of a side to rows (used for rotating).
# rotate_cube: Rotates the entire cube.
# swap_first_row: Swaps the first rows of two sides.
# swap_first_last_col: Swaps the first column of one side with the last column of another side.
# replace_side: Creates a copy of a given side.
# flip_forward, flip_backward, flip_cube: Flips the cube forward or backward.
# turn_front, turn_back, turn_left, turn_right, turn_top, turn_bottom: Rotates the cube in various directions to simulate moves.