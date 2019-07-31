import unittest
from Board import Board


class TestBoardUpMovement(unittest.TestCase):

    def setUp(self):
        self.before_1 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 5, 5: 8,
             6: 6, 7: 7, 8: 0}
        self.after_1 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 5, 5: 0,
             6: 6, 7: 7, 8: 8}

        self.before_2 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 5, 5: 0,
             6: 6, 7: 7, 8: 8}
        self.after_2 = \
            {0: 4, 1: 1, 2: 0,
             3: 3, 4: 5, 5: 2,
             6: 6, 7: 7, 8: 8}

        self.invalid = \
            {0: 0, 1: 1, 2: 2,
             3: 4, 4: 3, 5: 5,
             6: 6, 7: 7, 8: 8}

    def test(self):
        board = Board.from_previous(self.before_1)
        board1 = board.up()
        self.assertEqual(board1.tiles, self.after_1)

        board = Board.from_previous(self.before_2)
        board2 = board.up()
        self.assertEqual(board2.tiles, self.after_2)

        invalid_board = Board.from_previous(self.invalid)
        with self.assertRaises(Exception) as context:
            invalid_board.up()
        self.assertTrue("cannot move up" in str(context.exception))


class TestBoardDownMovement(unittest.TestCase):

    def setUp(self):
        self.before_1 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 0, 5: 5,
             6: 6, 7: 7, 8: 8}
        self.after_1 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 7, 5: 5,
             6: 6, 7: 0, 8: 8}

        self.before_2 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 5, 5: 0,
             6: 6, 7: 7, 8: 8}
        self.after_2 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 5, 5: 8,
             6: 6, 7: 7, 8: 0}

        self.invalid = \
            {0: 4, 1: 1, 2: 2,
             3: 6, 4: 3, 5: 5,
             6: 0, 7: 7, 8: 8}

    def test(self):
        board = Board.from_previous(self.before_1)
        board1 = board.down()
        self.assertEqual(board1.tiles, self.after_1)

        board = Board.from_previous(self.before_2)
        board2 = board.down()
        self.assertEqual(board2.tiles, self.after_2)

        invalid_board = Board.from_previous(self.invalid)
        with self.assertRaises(Exception) as context:
            invalid_board.down()
        self.assertTrue("cannot move down" in str(context.exception))


class TestBoardLeftMovement(unittest.TestCase):

    def setUp(self):
        self.before_1 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 0, 5: 5,
             6: 6, 7: 7, 8: 8}
        self.after_1 = \
            {0: 4, 1: 1, 2: 2,
             3: 0, 4: 3, 5: 5,
             6: 6, 7: 7, 8: 8}

        self.before_2 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 5, 5: 0,
             6: 6, 7: 7, 8: 8}
        self.after_2 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 0, 5: 5,
             6: 6, 7: 7, 8: 8}

        self.invalid = \
            {0: 4, 1: 1, 2: 2,
             3: 6, 4: 3, 5: 5,
             6: 0, 7: 7, 8: 8}

    def test(self):
        board = Board.from_previous(self.before_1)
        board1 = board.left()
        self.assertEqual(board1.tiles, self.after_1)

        board = Board.from_previous(self.before_2)
        board2 = board.left()
        self.assertEqual(board2.tiles, self.after_2)

        invalid_board = Board.from_previous(self.invalid)
        with self.assertRaises(Exception) as context:
            invalid_board.left()
        self.assertTrue("cannot move left" in str(context.exception))


class TestBoardRightMovement(unittest.TestCase):

    def setUp(self):
        self.before_1 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 0, 5: 5,
             6: 6, 7: 7, 8: 8}
        self.after_1 = \
            {0: 4, 1: 1, 2: 2,
             3: 3, 4: 5, 5: 0,
             6: 6, 7: 7, 8: 8}

        self.before_2 = \
            {0: 4, 1: 1, 2: 2,
             3: 6, 4: 3, 5: 5,
             6: 0, 7: 7, 8: 8}
        self.after_2 = \
            {0: 4, 1: 1, 2: 2,
             3: 6, 4: 3, 5: 5,
             6: 7, 7: 0, 8: 8}

        self.invalid = \
            {0: 4, 1: 1, 2: 2,
             3: 6, 4: 3, 5: 5,
             6: 8, 7: 7, 8: 0}

    def test(self):
        board = Board.from_previous(self.before_1)
        board1 = board.right()
        self.assertEqual(board1.tiles, self.after_1)

        board = Board.from_previous(self.before_2)
        board2 = board.right()
        self.assertEqual(board2.tiles, self.after_2)

        invalid_board = Board.from_previous(self.invalid)
        with self.assertRaises(Exception) as context:
            invalid_board.right()
        self.assertTrue("cannot move right" in str(context.exception))

if __name__ == '__main__':
    unittest.main()