import queue
from Board import Board
from Node import Node
import random
import heapq


class Algorithms:

    def __init__(self, array: []):
        board = Board.from_array(array)
        self.initial_state = Node(board)
        self.goal = Board.from_array([0,1, 2, 3, 4, 5, 6, 7, 8])
        return

    def bfs_search(self) -> 'bool':

        frontier = queue.Queue()
        expanded = 0
        frontier.put_nowait(self.initial_state)
        explored = []

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
                print(child.board.tiles)
                frontier.put_nowait(child)

        return False

    def a_star_search(self, initial_state: Board, goal: Board) -> 'bool':

        frontier = queue.PriorityQueue()
        explored = set()

        while not p_queue.empty():
            state = frontier.get_nowait()

            if state.board.tiles in explored:
                continue

            if state.board.__eq__(self.goal):

                return True
        return

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
            'actions': self.actions,
            'solution': self.tiles
        }
