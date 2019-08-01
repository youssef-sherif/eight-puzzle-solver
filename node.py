from Board import Board
from Queue import Queue

class Node:
    children = []

    def __init__(self, input_board: Board):

        self.board = input_board
        self.up = None
        self.down = None
        self.left = None
        self.rigth = None
        return

    @classmethod
    def from_node(cls, input_board: Board, parent: 'Node'):

        cls.parent = parent
        return cls(input_board)

    def get_board(self):
        return self.board

    def set_up(self):
        try:

            # print(self.board.tiles)
            # print(self.board.up().tiles)
            # print(self.board.tiles)
            self.up = Node.from_node(self.board.up(), self)
            self.children.append(self.up)
            return self.up
        except Exception as e:
            print(e)
    def set_down(self):
        try:
            self.down = Node.from_node(self.board.down(),self)
            self.children.append(self.down)
        except Exception as e:
            print(e)
        return self.down

    def set_left(self):
        try:
            self.left = Node.from_node(self.board.left(),self)
            self.children.append(self.left)
        except Exception as e:
            print(e)
        return self.left

    def set_right(self):
        try:
            self.rigth = Node.from_node(self.board.right(),self)
            self.children.append(self.rigth)
        except Exception as e:
            print(e)
        return self.rigth

    def set_children(self):
        self.set_up()
        self.set_down()
        self.set_left()
        self.set_right()
        return

    def get_neighbours(self):
        neighbours = [self.parent]
        neighbours.extend(self.children)
        return neighbours

    def build_tree(self):
        
        return
#
# class Tree:
#
#     list = []
#
#     # def build(self,root: Node):
#     #     self.list.append(root.set_up())
#     #     self.list.append(root.set_down())
#     #     self.list.append(root.set_left())
#     #     self.list.append(root.set_right())
#     #     if len(self.list)<30:
#     #         for child in root.children:
#     #             self.build(child)
#     #     return
#     #
#     # def build(self,root : Node):
#     #     queue = Queue()
#     #     queue.enqueue(self.root.set_up())
#     #     queue.enqueue(self.root.set_down())
#     #     queue.enqueue(self.root.set_left())
#     #     queue.enqueue(self.root.set_right())
#     #     while queue.length >0 and queue.length<30:
#     #
#     #     return
#     #
#     def __init__(self,board : Board):
#         self.root = Node(board)
#         self.build(self.root)
#         return
#
#
#     def insert(self, node: Node):
#         self.list.append([node])
#
#     def get_child(self, node: Node):
#         return