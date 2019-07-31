from Board import Board
# from Queue import Queue

class Node:
    children = []
    def __init__(self, input_board: Board):
        self.board = input_board
        self.up = None
        self.down = None
        self.left = None
        self.rigth = None
        self.parent = None
        return

    def get_board(self):
        return self.board

    def set_up(self):
        self.up = Node(self.board.up())
        self.children.append(self.up)
        return self.up

    def set_down(self):
        self.down = self.board.down()
        self.children.append(self.down)
        return self.down

    def set_left(self):
        self.left = self.board.left()
        self.children.append(self.left)
        return self.left

    def set_right(self):
        self.rigth = self.board.right()
        self.children.append(self.rigth)
        return self.rigth
class Tree:

    list = []

    # def build(self,root: Node):
    #     self.list.append(root.set_up())
    #     self.list.append(root.set_down())
    #     self.list.append(root.set_left())
    #     self.list.append(root.set_right())
    #     if len(self.list)<30:
    #         for child in root.children:
    #             self.build(child)
    #     return
    #
    # def build(self,root : Node):
    #     queue = Queue()
    #     queue.enqueue(self.root.set_up())
    #     queue.enqueue(self.root.set_down())
    #     queue.enqueue(self.root.set_left())
    #     queue.enqueue(self.root.set_right())
    #     while queue.length >0 and queue.length<30:
    #
    #     return
    #
    def __init__(self,board : Board):
        self.root = Node.__init__(board)
        self.build(self.root)
        return


    def insert(self, node: Node):
        self.list.append([node])

    def get_child(self, node: Node):
        return