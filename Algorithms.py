import queue
import heapq
from Board import Board
from Node import Node
import random
from sklearn.neighbors import DistanceMetric
import numpy as np
import time


class Algorithms:

    def __init__(self, array: []):
        board = Board.from_array(array)
        self.initial_state = Node(board)
        self.goal = Board.from_array([0,1, 2, 3, 4, 5, 6, 7, 8])
        self.expanded = 0
        self.actions_taken = []
        self.time = 0
        return

    def bfs_search(self) -> 'bool':

        startTime = time.time()

        frontier = queue.Queue()
        expanded = 0
        frontier.put_nowait(self.initial_state)
        explored = []

        while not frontier.empty():
            state = frontier.get_nowait()

            print(list(state.board.tiles.values()))

            if state.board.__eq__(self.goal):
                self.expanded = expanded
                nodes = state.backtrack()
                for node in nodes:
                    self.actions_taken.append(node.action_taken)

                self.time = time.time() - startTime
                return True

            explored.append(state.board.tiles)
            expanded += 1

            state.set_children()

            for neighbour in state.get_neighbours():
                if neighbour is not None:
                    if neighbour.board.tiles not in list(frontier.queue) and neighbour.board.tiles not in explored:
                        frontier.put_nowait(neighbour)

        return False

    def a_star_search(self, heuristic: str) -> 'bool':

        startTime = time.time()

        explored = []
        expanded = 0

        if heuristic == 'euclidean':
            dist = DistanceMetric.get_metric('euclidean')
        elif heuristic == 'manhattan':
            dist = DistanceMetric.get_metric('manhattan')

        X = [list(self.initial_state.board.tiles.values()),
             list(self.goal.tiles.values())]

        self.initial_state.set_distance(dist.pairwise(X))

        heap_list = [self.initial_state]
        heapq.heapify(heap_list)

        while True:
            state = heap_list.pop()
            print(list(state.board.tiles.values()))

            if state.board.__eq__(self.goal):
                self.expanded = expanded
                nodes = state.backtrack()
                for node in nodes:
                    self.actions_taken.append(node.action_taken)

                self.time = time.time() - startTime
                return True

            explored.append(state.board.tiles)
            expanded += 1

            state.set_children()

            for neighbour in state.get_neighbours():
                if neighbour is not None:

                    neighbour.set_distance(dist.pairwise(
                        [list(neighbour.board.tiles.values()),
                         list(self.goal.tiles.values())]
                    ))

                    if neighbour in heap_list:
                        if np.less(neighbour.distance, np.add(neighbour.distance, state.distance)).all():
                            heap_list.remove(neighbour)
                            heapq.heapify(heap_list)

                    if neighbour.board.tiles in explored:
                        if np.less(neighbour.distance, np.add(neighbour.distance, state.distance)).all():
                            explored.remove(neighbour.board.tiles)

                    if neighbour not in heap_list and neighbour.board.tiles not in explored:
                        heap_list.insert(0, neighbour)
                        heapq.heapify(heap_list)
                        neighbour.parent = state


        return False

    def dfs_search(self, initial_state: Board, goal: Board) -> 'bool':

        frontier = queue.LifoQueue(maxsize=32)
        frontier.put_nowait(initial_state)
        explored = set()

        while not frontier.empty():
            state = frontier.get_nowait()
            explored.add(state)

            if state.__eq__(goal):
                return True

            for neighbor in state.neighbors():
                if neighbor not in frontier and neighbor not in explored:
                    frontier.put_nowait(neighbor)

        return False

    def solution_json(self):

        return {
            'actions': self.actions_taken,
            'nodes_expanded': self.expanded,
            'time': self.time
        }
