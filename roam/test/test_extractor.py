import unittest
from detector.extractor import *


class TestExtractor(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def test_tuple_by_ends(self):
        self.assertEqual((), tuple_by_ends([]))
        self.assertEqual((1,), tuple_by_ends([1]))
        self.assertEqual((3,), tuple_by_ends([3]))
        self.assertEqual((1, 2,), tuple_by_ends([1, 2]))
        self.assertEqual((3, 4, 5, 6,), tuple_by_ends([3, 6]))
        self.assertEqual((3, 4, 5,), tuple_by_ends([5, 3]))
        self.assertEqual((6, 7,), tuple_by_ends([6, 7]))

    def test_season(self):
        self.assertEqual((1,), extract_seasons('S1'))
        self.assertEqual((1,), extract_seasons('S 1'))
        self.assertEqual((1,), extract_seasons('S01'))
        self.assertEqual((1,), extract_seasons('S 01'))
        self.assertEqual((1,), extract_seasons('S01E01'))
        self.assertEqual((1,), extract_seasons('1 S01 '))
        self.assertEqual((1,), extract_seasons('.S01.'))
        self.assertEqual((), extract_seasons('aS01a'))
        self.assertEqual((), extract_seasons('KBSS01'))
        self.assertEqual((1,), extract_seasons('1x07'))
        self.assertEqual((1, 2, 3,), extract_seasons('S01-S03'))
        self.assertEqual((1,), extract_seasons('Season1'))
        self.assertEqual((1,), extract_seasons('Season01'))
        self.assertEqual((1,), extract_seasons('Season 01'))
        self.assertEqual((1, 2, 3,), extract_seasons('Season01~Season03'))
        self.assertEqual((1, 2, 3,), extract_seasons('Season 01~Season 03'))
        self.assertEqual((1,), extract_seasons('시즌1'))
        self.assertEqual((1,), extract_seasons('시즌01'))
        self.assertEqual((1,), extract_seasons('시즌 1'))
        self.assertEqual((3, 4,), extract_seasons('시즌3-시즌4'))
        self.assertEqual((3, 4, 5,), extract_seasons('시즌 3-시즌 5'))
        self.assertEqual((3, 4, 5,), extract_seasons('시즌03-시즌05'))
        self.assertEqual((3, 4,), extract_seasons('시즌3 - 시즌4'))
        self.assertEqual((4, 5, 6, 7, 8), extract_seasons('시즌8 - 시즌4'))

    def test_episide(self):
        self.assertEqual((1,), extract_episode('E01'))
        self.assertEqual((1, 2, 3, ), extract_episode('E01-E03'))
        self.assertEqual((4, 5, ), extract_episode('E04-E05'))
        self.assertEqual((4, 5, ), extract_episode('Episode04-Episode05'))
        self.assertEqual((1,), extract_episode('Episode1'))
        self.assertEqual((4,), extract_episode('4화'))
        self.assertEqual((4,), extract_episode('4회'))

    def test_date(self):
        self.assertEqual(('140530', ), extract_date('140530'))
        self.assertEqual(('140530', '140531'), extract_date('140530~140531'))
