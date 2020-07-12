import unittest
import Game
from Board import Board


def runTest(moves):
    board = Board()
    Game.doMoves(moves, board)
    return board.toString()


class Tests(unittest.TestCase):
    # trying to move in check
    def test2(self):
        moves = "e2-e3 d7-d5 Bf1-b5+ a7-a6"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|p|_|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|B|_|p|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|P|_|_|_|\n"
                    "2|P|P|P|P|_|P|P|P|\n"
                    "1|R|N|B|Q|K|_|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    # capturing
    def test3(self):
        moves = "Nb1-c3 e7-e5 a2-a3 Bf8-b4 a3-a4 Bb4xNc3"
        expected = ("8|r|n|b|q|k|_|n|r|\n"
                    "7|p|p|p|p|_|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|p|_|_|_|\n"
                    "4|P|_|_|_|_|_|_|_|\n"
                    "3|_|_|b|_|_|_|_|_|\n"
                    "2|_|P|P|P|P|P|P|P|\n"
                    "1|R|_|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test4(self):
        moves = "e2-e3 b7-b6 Qd1-f3 b6-b5 Qf3xRa8"
        expected = ("8|Q|n|b|q|k|b|n|r|\n"
                    "7|p|_|p|p|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|p|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|P|_|_|_|\n"
                    "2|P|P|P|P|_|P|P|P|\n"
                    "1|R|N|B|_|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test5(self):
        moves = "e2-e3 b7-b6 Qd1-f3 Bc8-b7 a2-a3 Bb7xQf3"
        expected = ("8|r|n|_|q|k|b|n|r|\n"
                    "7|p|_|p|p|p|p|p|p|\n"
                    "6|_|p|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|P|_|_|_|P|b|_|_|\n"
                    "2|_|P|P|P|_|P|P|P|\n"
                    "1|R|N|B|_|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test6(self):
        moves = "d2-d4 Ng8-f6 Bc1-g5 d7-d6 Bg5xNf6"
        expected = ("8|r|n|b|q|k|b|_|r|\n"
                    "7|p|p|p|_|p|p|p|p|\n"
                    "6|_|_|_|p|_|B|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|P|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|P|P|P|_|P|P|P|P|\n"
                    "1|R|N|_|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test7(self):
        moves = "e2-e3 b7-b6 Qd1-f3 Bc8-b7 a2-a3 Bb7xQf3"
        expected = ("8|r|n|_|q|k|b|n|r|\n"
                    "7|p|_|p|p|p|p|p|p|\n"
                    "6|_|p|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|P|_|_|_|P|b|_|_|\n"
                    "2|_|P|P|P|_|P|P|P|\n"
                    "1|R|N|B|_|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test8(self):
        moves = "d2-d4 h7-h6 Bc1-g5 h6xBg5"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|p|p|p|p|p|_|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|p|_|\n"
                    "4|_|_|_|P|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|P|P|P|_|P|P|P|P|\n"
                    "1|R|N|_|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test9(self):
        moves = "d2-d4 e7-e6 Bc1-g5 d7-d6 Bg5xQd8"
        expected = ("8|r|n|b|B|k|b|n|r|\n"
                    "7|p|p|p|_|_|p|p|p|\n"
                    "6|_|_|_|p|p|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|P|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|P|P|P|_|P|P|P|P|\n"
                    "1|R|N|_|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test10(self):
        moves = "b2-b3 g7-g6 b3-b4 Bf8-g7 b4-b5 Bg7xRa1"
        expected = ("8|r|n|b|q|k|_|n|r|\n"
                    "7|p|p|p|p|p|p|_|p|\n"
                    "6|_|_|_|_|_|_|p|_|\n"
                    "5|_|P|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|P|_|P|P|P|P|P|P|\n"
                    "1|b|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test11(self):
        moves = "a2-a4 h7-h5 Ra1-a3 Rh8-h6 Ra3-d3 Rh6-g6 Rd3xd7"
        expected = ("8|r|n|b|q|k|b|n|_|\n"
                    "7|p|p|p|R|p|p|p|_|\n"
                    "6|_|_|_|_|_|_|r|_|\n"
                    "5|_|_|_|_|_|_|_|p|\n"
                    "4|P|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|_|P|P|P|P|P|P|P|\n"
                    "1|_|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    # castling
    def test12(self):
        moves = "Ng1-f3 a7-a6 e2-e3 a6-a5 Bf1-e2 a5-a4 O-O"
        expected = ("8|r|n|b|q|k|b|n|r|\n" +
                    "7|_|p|p|p|p|p|p|p|\n" +
                    "6|_|_|_|_|_|_|_|_|\n" +
                    "5|_|_|_|_|_|_|_|_|\n" +
                    "4|p|_|_|_|_|_|_|_|\n" +
                    "3|_|_|_|_|P|N|_|_|\n" +
                    "2|P|P|P|P|B|P|P|P|\n" +
                    "1|R|N|B|Q|_|R|K|_|\n" +
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test13(self):
        moves = "Nb1-c3 a7-a6 d2-d3 a6-a5 Bc1-e3 a5-a4 Qd1-d2 a4-a3 O-O-O"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|_|p|p|p|p|p|p|p|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|p|_|N|P|B|_|_|_|\n"
                    "2|P|P|P|Q|P|P|P|P|\n"
                    "1|_|_|K|R|_|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test14(self):
        moves = "a2-a3 Nb8-c6 a3-a4 d7-d6 a4-a5 Bc8-e6 h2-h3 Qd8-d7 h3-h4 O-O-O"
        expected = ("8|_|_|k|r|_|b|n|r|\n"
                    "7|p|p|p|q|p|p|p|p|\n"
                    "6|_|_|n|p|b|_|_|_|\n"
                    "5|P|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|P|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|_|P|P|P|P|P|P|_|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    # en passen
    def test14(self):
        moves = "a2-a4 h7-h6 a4-a5 b7-b5 a5xb6ep"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|_|p|p|p|p|p|_|\n"
                    "6|_|P|_|_|_|_|_|p|\n"
                    "5|_|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|_|_|\n"
                    "2|_|P|P|P|P|P|P|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    def test15(self):
        moves = "a2-a4 h7-h5 a4-a5 h5-h4 g2-g4 h4xg3ep"
        expected = ("8|r|n|b|q|k|b|n|r|\n"
                    "7|p|p|p|p|p|p|p|_|\n"
                    "6|_|_|_|_|_|_|_|_|\n"
                    "5|P|_|_|_|_|_|_|_|\n"
                    "4|_|_|_|_|_|_|_|_|\n"
                    "3|_|_|_|_|_|_|p|_|\n"
                    "2|_|P|P|P|P|P|_|P|\n"
                    "1|R|N|B|Q|K|B|N|R|\n"
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)

    # promotion
    def test16(self):
        moves = "a2-a4 h7-h6 a4-a5 b7-b5 a5xb6ep Nb8-c6 b6-b7 g7-g6 b7-b8=Q"
        expected = ("8|r|Q|b|q|k|b|n|r|\n" +
                    "7|p|_|p|p|p|p|_|_|\n" +
                    "6|_|_|n|_|_|_|p|p|\n" +
                    "5|_|_|_|_|_|_|_|_|\n" +
                    "4|_|_|_|_|_|_|_|_|\n" +
                    "3|_|_|_|_|_|_|_|_|\n" +
                    "2|_|P|P|P|P|P|P|P|\n" +
                    "1|R|N|B|Q|K|B|N|R|\n" +
                    "  a b c d e f g h")
        self.assertEqual(runTest(moves), expected)
