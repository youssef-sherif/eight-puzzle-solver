def empty_tile(tiles: {}):
    for tile in tiles.keys():
        if tiles[tile] == 0:
            return tile


class Board:
    tiles = {}

    def __init__(self):
        return

    @classmethod
    def from_dictionary(cls, tiles: {}) -> 'Board':
        cls.tiles = tiles
        return cls()

    def build(self):
        for i in range(0, 9):
            self.tiles[i] = int(input("Enter tile " + str(i) + " value: "))
        self.tiles["empty_tile"] = empty_tile(self.tiles)

    def validate(self):
        return

    def up(self) -> 'Board':
        if self.can_move_up():
            board = Board.from_dictionary(self.tiles)
            temp = int(board.tiles[board.tiles["empty_tile"]-3])
            board.tiles[board.tiles["empty_tile"] - 3]= board.tiles[board.tiles["empty_tile"]]
            board.tiles[board.tiles["empty_tile"]] = temp
            board.tiles["empty_tile"]= board.tiles["empty_tile"]-3
            return board
        else:
            raise Exception("cannot move up")

    def down(self):
        return

    def left(self):
        return

    def right(self):
        return

    def can_move_up(self) -> 'bool':
        if int(self.tiles["empty_tile"]) == 0 or int(self.tiles["empty_tile"]) == 1 or int(self.tiles["empty_tile"]) == 2:
            return False
        else:
            return True

    def can_move_down(self) -> 'bool':
        if int(self.tiles["empty_tile"]) == 6 or int(self.tiles["empty_tile"]) == 7 or int(self.tiles["empty_tile"]) == 8:
            return False
        else:
            return True

    def can_move_left(self) -> 'bool':
        if int(self.tiles["empty_tile"]) == 0 or int(self.tiles["empty_tile"]) == 3 or int(self.tiles["empty_tile"]) == 6:
            return False
        else:
            return True

    def can_move_right(self) -> 'bool':
        if int(self.tiles["empty_tile"]) == 2 or int(self.tiles["empty_tile"]) == 5 or int(self.tiles["empty_tile"]) == 8:
            return False
        else:
            return True
