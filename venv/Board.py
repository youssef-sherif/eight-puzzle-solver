#############
# Board class
#############

class Board:
    tiles = {}

    def __init__(self):
        return

    @classmethod
    def from_dictionary(cls, tiles: {}) -> 'Board':
        cls.tiles = tiles
        cls.empty_tile_location = get_empty_tile_location(cls.tiles)

        return cls()

    @classmethod
    def from_input(cls, size: int) -> 'Board':
        for i in range(0, size):
            cls.tiles[i] = int(input("Enter tile " + str(i) + " value: "))
            print(cls.tiles)
        cls.empty_tile_location = get_empty_tile_location(cls.tiles)

        return cls()

    def up(self) -> 'Board':
        if self.can_move_up():
            board = swap(self.empty_tile_location - 3, self.empty_tile_location, self)

            return board
        else:
            raise Exception("cannot move up")

    def down(self) -> 'Board':
        if self.can_move_down():
            board = swap(self.empty_tile_location + 3, self.empty_tile_location, self)

            return board
        else:
            raise Exception("cannot move down")

    def left(self) -> 'Board':
        if self.can_move_left():
            board = swap(self.empty_tile_location - 1, self.empty_tile_location, self)

            return board
        else:
            raise Exception("cannot move left")

    def right(self) -> 'Board':
        if self.can_move_right():
            board = swap(self.empty_tile_location + 1, self.empty_tile_location, self)

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


def swap(x: int, y: int, old_board: Board) -> 'Board':
    board = Board.from_dictionary(old_board.tiles)
    temp = board.tiles[x]
    board.tiles[x] = board.tiles[y]
    board.tiles[y] = temp

    return board
