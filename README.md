# eight-puzzle-solver
An AI program that solves the famous 8 puzzle problem using different Search Techniques

# Search Algorithms Used:
 - BFS
 - DFS
 - AStar

# Installation
 ```
  $ pip3 install sklearn
  $ python3 main.py
 ```
 
# Sample Run Using AStar Algorithm and manhattan approximation
```
1 2 5
3 4 0
6 7 8
```
```
1 2 0
3 4 5
6 7 8
```
```
1 0 2
3 4 5
6 7 8
```
```
0 1 2
3 4 5
6 7 8
```

{'nodes_expanded': 4, 'time': 0.0008945465087890625, 'actions': ['start', 'up', 'left', 'left']}
