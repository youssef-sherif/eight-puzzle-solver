from Algorithms import Algorithms
import random
import time

random_array = random.sample(range(0, 9), 9)

algorithms = Algorithms([1, 2, 5,
                         3, 4, 0,
                         6, 7, 8])
# algorithms = Algorithms(random_array)

done = False
done = algorithms.dfs_search()
if done:
    print(algorithms.solution_json())
#
# done = algorithms.bfs_search()
# if done:
#     print(algorithms.solution_json())

# done = algorithms.a_star_search('manhattan')
# if done:
#     print(algorithms.solution_json())