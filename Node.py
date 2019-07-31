from Board import Board
# from Queue import Queue

class Node:
    children = []
    
    def __init__(self, input_board: Board):

        self.board = input_board
        self.up = None
        self.down = None
        self.left = None
        self.right = None

        return

    @classmethod
    def from_node(cls, input_board: Board, parent: 'Node'):

        cls.parent = parent
        return cls(input_board)

    def get_board(self):
        return self.board

    def set_up(self):
        try:
            self.up = Node.from_node(self.board.up(), self)
            self.children.append(self.up)
            print('move up')
        except Exception as e:
            print(e)
        return self.up

    def set_down(self):
        try:
            self.down = Node.from_node(self.board.down(),self)
            self.children.append(self.down)
            print('move down')
        except Exception as e:
            print(e)
        return self.down

    def set_left(self):
        try:
            self.left = Node.from_node(self.board.left(),self)
            self.children.append(self.left)
            print('move left')
        except Exception as e:
            print(e)
        return self.left

    def set_right(self):
        try:
            self.right = Node.from_node(self.board.right(),self)
            self.children.append(self.right)
            print('move right')
        except Exception as e:
            print(e)
        return self.right

    def set_children(self):
        self.set_up()
        self.set_down()
        self.set_left()
        self.set_right()

    def get_neighbours(self):
        neighbours = [self.parent]
        neighbours.extend(self.children)
        return neighbours