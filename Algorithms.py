import queue
from Board import Board
from Node import Node
import random
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import DistanceMetric


class Algorithms:

    def __init__(self, array: []):
        board = Board.from_array(array)
        self.initial_state = Node(board)
        self.goal = Board.from_array([0,1, 2, 3, 4, 5, 6, 7, 8])
        self.expanded = 0
        return

    def bfs_search(self) -> 'bool':

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
                actions_taken = []
                for node in nodes:
                    actions_taken.append(node.action_taken)

                print(actions_taken)

                return True

            explored.append(state.board.tiles)
            expanded += 1

            state.set_children()

            for child in state.children:
                if child.board.tiles not in list(frontier.queue) and child.board.tiles not in explored:
                    frontier.put_nowait(child)

        return False

    def a_star_search(self, heuristic: str) -> 'bool':

        frontier = queue.PriorityQueue()
        explored = []
        expanded = 0
        frontier.put_nowait(self.initial_state)

        while not frontier.empty():
            state = frontier.get_nowait()

            if state.board.tiles in explored:
                continue

            if state.board.__eq__(self.goal):
                return True

            explored.append(state.board.tiles)
            expanded += 1

            state.set_children()

            for child in state.children:
                if heuristic == 'euclidean':
                    dist = DistanceMetric.get_metric('euclidean')
                    X = [list(child.board.tiles.values()),
                         list(self.goal.tiles.values())]
                    print(X)
                    array = dist.pairwise(X)
                    print(array)
                    frontier.put_nowait(array)

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
            # 'actions': self.actions,
            # 'solution': self.tiles,
            'nodes_expanded': self.expanded
        }
