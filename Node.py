from Board import Board
import numpy as np


class Node:
    children = []
    
    def __init__(self, input_board: Board):

        self.board = input_board
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.parent = None
        self.action_taken = "start"
        self.distance = []

    def __lt__(self, other):
        return np.greater_equal(self.distance, other.distance).all()

    @classmethod
    def from_node(cls, input_board: Board, parent: 'Node'):
        cls.parent = parent

        return cls(input_board)

    def get_board(self):
        return self.board

    def set_up(self):
        try:
            self.up = Node.from_node(self.board.up(), self)
            self.up.parent = self
            self.up.action_taken = 'up'
            self.children.append(self.up)
        except Exception as e:
            print(e)
        return self.up

    def set_down(self):
        try:
            self.down = Node.from_node(self.board.down(),self)
            self.down.parent = self
            self.down.action_taken = 'down'
            self.children.append(self.down)
        except Exception as e:
            print(e)
        return self.down

    def set_left(self):
        try:
            self.left = Node.from_node(self.board.left(),self)
            self.left.parent = self
            self.left.action_taken = 'left'
            self.children.append(self.left)
        except Exception as e:
            print(e)
        return self.left

    def set_right(self):
        try:
            self.right = Node.from_node(self.board.right(),self)
            self.right.parent = self
            self.right.action_taken = 'right'
            self.children.append(self.right)
        except Exception as e:
            print(e)
        return self.right

    def set_children(self):
        self.set_up()
        self.set_down()
        self.set_left()
        self.set_right()

    def backtrack(self) -> []:
        nodes = []
        node = self
        while node is not None:
            nodes.append(node)
            node = node.parent
        return nodes[::-1]

    def get_neighbours(self):
        neighbours = [self.parent]
        neighbours.extend(self.children)
        return neighbours

    def set_distance(self, distance):
        self.distance = distance