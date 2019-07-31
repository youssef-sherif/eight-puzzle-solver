# from sklearn.metrics.pairwise import manhattan_distances
# from sklearn.neighbors import DistanceMetric
# from Board import Board
#
# board = Board.from_input(9)
#
# try:
#     board = board.up()
#     print(board.tiles)
# except Exception as e:
#     print(e)
import random
###########################
# this will be useful later
###########################
# manhattan_distances(X, Y=None, sum_over_features=True)
# dist = DistanceMetric.get_metric('euclidean')
# X = [[0, 1, 2],
#          [3, 4, 5]]
#
# array = dist.pairwise(X)

from Tree import Node
from Board import Board
x= random.sample(range(0, 9), 9)
try:
    board= Board.from_array(x)
except Exception as e:
    print(e)
node = Node(board)
node.set_up()
# print(node.board.tiles)
# node.set_children()
# print(node.board.up().tiles)
# for child in node.children:
#     print(child.board.tiles)
# print(node.children)