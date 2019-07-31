from sklearn.metrics.pairwise import manhattan_distances
from sklearn.neighbors import DistanceMetric
from Board import Board
import random
import copy

try:
    original = Board.from_array(random.sample(range(0, 9), 9))
    print(original)
    print(original.tiles)
    board1 = original.up()
    print(board1)
    print(board1.tiles)
    board2 = board1.up()
    print(board2)
    print(board2.tiles)

    print("original values:")
    print(original)
    print(original.tiles)
    print(board1)
    print(board1.tiles)
    print(board2)
    print(board2.tiles)
except Exception as e:
    print(e)

###########################
# this will be useful later
###########################
# manhattan_distances(X, Y=None, sum_over_features=True)
# dist = DistanceMetric.get_metric('euclidean')
# X = [[0, 1, 2],
#          [3, 4, 5]]
#
# array = dist.pairwise(X)
