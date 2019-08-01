from node import Node
from Stack import Stack
class DFS:
    def __init__(self):
        return
    def search(self,root) ->'bool':
        frontier = Stack
        explored = list()
        while not frontier.is_empty():
            state = frontier.pop()
            explored.append(state)
            if state.board.__eq__(self.goal):
                return True
            for neighbour in state.get_neigbours:
                if neighbour not in frontier.stack and neighbour not in explored: ######---> frontier union explored
                    frontier.push(neighbour)
        return False`

        return
