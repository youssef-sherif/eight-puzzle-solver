import queue
from Board import Board
import heapq


def bfs_search(initial_state: Board, goal: Board) -> 'bool':

    frontier = queue.Queue(maxsize=32)
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


def dfs_search(initial_state: Board, goal: Board) -> 'bool':

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


def a_star_search(initial_state: Board, goal: Board) -> 'bool':

    heapq.heapify([initial_state])
    explored = set()

    return