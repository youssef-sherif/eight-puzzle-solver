import queue
import heapq
from Board import Board
from Node import Node
from Stack import Stack
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

        start_time = time.time()

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

                self.time = time.time() - start_time
                return True

            explored.append(state.board.tiles)
            expanded += 1

            state.set_children()

            for neighbour in state.get_neighbours():
                if neighbour is not None:
                    if neighbour.board.tiles not in list(frontier.queue) and neighbour.board.tiles not in explored:
                        frontier.put_nowait(neighbour)

        return False

    def dfs_search(self) ->'bool':

        start_time = time.time()

        depth = 0
        limit = 100
        frontier = Stack()
        explored = list()
        frontier.push(self.initial_state)
        while not frontier.is_empty():

            print(frontier.stack)
            state = frontier.pop()

            if limit >= depth:

                explored.append(state.board.tiles)
                self.expanded += 1
                print(state.board.tiles)
                print(explored)
                print(explored.__len__())
                print(frontier.stack.__len__())
                print(depth)
                if state.board.__eq__(self.goal):
                    self.finalize(state)
                    self.time = time.time() - start_time
                    return True
                state.set_children()
                for neighbour in state.get_neighbours():
                    if neighbour is not None and neighbour not in frontier.stack and neighbour.board.tiles not in explored: ######---> frontier union explored
                        frontier.push(neighbour)
                        depth += 1
            else:
                depth -= 1
                continue
        return False


    def a_star_search(self, heuristic: str) -> 'bool':

        start_time = time.time()

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

                self.time = time.time() - start_time
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

    def solution_json(self):

        return {
            'nodes_expanded': self.expanded,
            'time': self.time,
            'actions': self.actions_taken,
        }

    def finalize(self,state: Node):
        nodes = state.backtrack()
        for node in nodes:
            self.actions_taken.append(node.action_taken)

