from Algorithms import Algorithms
import random
#
random_array = random.sample(range(0, 9), 9)

algorithms = Algorithms([1, 2, 5,
                         3, 4, 0,
                         6, 7, 8])
# algorithms = Algorithms(random_array)

done = False
done = algorithms.dfs_search()

# done = algorithms.a_star_search('manhattan')
if done:
    print(algorithms.solution_json())
else:
    print("false")