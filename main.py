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
from Algorithms import Algorithms
import random
#
random_array = random.sample(range(0, 9), 9)
algorithms = Algorithms([1, 4, 2,
                         3, 0, 5,
                         6, 7, 8])

done = False
done = algorithms.bfs_search()

# done = algorithms.a_star_search('euclidean')

if done:
    print(algorithms.solution_json())

