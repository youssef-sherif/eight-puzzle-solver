import queue
from Board import Board
import heapq


class Algorithms:

    def __init__(self):
        board = Board.from_array(random.sample(range(0, 9), 9))
        self.initialState = Node(board)
        return

    def bfs_search(self) -> 'bool':

        frontier = queue.Queue(maxsize=32)
        frontier.put_nowait(self.initial_state)
        explored = set()

        while not frontier.empty():
            state = frontier.get_nowait()
            explored.add(state)

            if state.__eq__(self.goal):

                return True

            for neighbor in state.get_neighbours():
                if neighbor not in frontier and neighbor not in explored:
                    frontier.put_nowait(neighbor)

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


    def a_star_search(self, initial_state: Board, goal: Board) -> 'bool':

        heapq.heapify([initial_state])
        explored = set()

        return

    def solution_json(self):

        return {
            'actions': self.actions,
            'solution': self.tiles
        }
