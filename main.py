###########################
# this will be useful later
###########################
# manhattan_distances(X, Y=None, sum_over_features=True)
# dist = DistanceMetric.get_metric('euclidean')
# X = [[0, 1, 2],
#          [3, 4, 5]]
#
# array = dist.pairwise(X)

from Node import Node
from Board import Board
#
# x= random.sample(range(0, 9), 9)
# try:
#     board= Board.from_array(x)
# except Exception as e:
#     print(e)
# node = Node(board)
# print(node.board)
# node.set_children()
# print(node.parent.board)
# # # print(node.board.up().tiles)
# # for child in node.children:
# #     print(child.board.tiles)
# # print(node.children)
# # print(node.board.tiles)
# =======
from Algorithms import Algorithms
import random
import time
start = time.time()
#
random_array = random.sample(range(0, 9), 9)
algorithms = Algorithms([3, 1, 2,
                         6, 4, 5,
                         0, 7, 8])

# algorithms = Algorithms(random_array)

done = False
done = algorithms.dfs_search()

# done = algorithms.a_star_search('euclidean')

if done:
    print(algorithms.solution_json())
else:
    print("false")

end = time.time()
print(str(end-start) + "  seconds")