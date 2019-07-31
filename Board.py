#############
# Board class
#############


class Board:
    tiles = {}
    actions = list()

    def __eq__(self, board: 'Board') -> 'bool':
        for key in list(self.tiles.keys()):
            if key not in list(board.tiles.keys()):
                return False
        return True

    def __init__(self):
        return

    @classmethod
    def from_previous(cls, tiles: {}) -> 'Board':
        cls.tiles = tiles
        cls.empty_tile_location = int(get_empty_tile_location(cls.tiles))

        return cls()

    @classmethod
    def from_array(cls, numbers: []) -> 'Board':
        tiles = {}
        cls.actions = list()
        for i in range(0, 9):
            tiles[i] = numbers[i]
        cls.tiles = tiles
        cls.empty_tile_location = int(get_empty_tile_location(cls.tiles))

        return cls()

    def solution_json(self):

        return {
            'actions': self.actions,
            'solution': self.tiles
        }

    def up(self) -> 'Board':
        if self.can_move_up():
            board = Board.from_previous(self.tiles)
            board = swap(self.empty_tile_location - 3, self.empty_tile_location, board)
            self.actions.insert(self.actions.__len__(), 'up')

            return board
        else:
            raise Exception("cannot move up")

    def down(self) -> 'Board':
        if self.can_move_down():
            board = Board.from_previous(self.tiles)
            board = swap(self.empty_tile_location + 3, self.empty_tile_location, board)
            self.actions.insert(self.actions.__len__(), 'down')

            return board
        else:
            raise Exception("cannot move down")

    def left(self) -> 'Board':
        if self.can_move_left():
            board = Board.from_previous(self.tiles)
            board = swap(self.empty_tile_location - 1, self.empty_tile_location, board)
            self.actions.insert(self.actions.__len__(), 'left')

            return board
        else:
            raise Exception("cannot move left")

    def right(self) -> 'Board':
        if self.can_move_right():
            board = Board.from_previous(self.tiles)
            board = swap(self.empty_tile_location + 1, self.empty_tile_location, board)
            self.actions.insert(self.actions.__len__(), 'right')

            return board
        else:
            raise Exception("cannot move right")

    def can_move_up(self) -> 'bool':
        return not (int(self.empty_tile_location) == 0 or int(self.empty_tile_location) == 1 or int(
            self.empty_tile_location) == 2)

    def can_move_down(self) -> 'bool':
        return not (int(self.empty_tile_location) == 6 or int(self.empty_tile_location) == 7 or int(
            self.empty_tile_location) == 8)

    def can_move_left(self) -> 'bool':
        return not (int(self.empty_tile_location) == 0 or int(self.empty_tile_location) == 3 or int(
            self.empty_tile_location) == 6)

    def can_move_right(self) -> 'bool':
        return not (int(self.empty_tile_location) == 2 or int(self.empty_tile_location) == 5 or int(
            self.empty_tile_location) == 8)


################
# helper methods
################


def get_empty_tile_location(tiles: {}) -> 'int':
    for tile in tiles.keys():
        if tiles[tile] == 0:
            return tile


def swap(x: int, y: int, board: 'Board') -> 'Board':
    temp = board.tiles[x]
    board.tiles[x] = board.tiles[y]
    board.tiles[y] = temp

    return board

