from sklearn.metrics.pairwise import manhattan_distances
from sklearn.neighbors import DistanceMetric
from Board import Board

board = Board.from_input(9)

try:
    board = board.up()
    print(board.tiles)
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
