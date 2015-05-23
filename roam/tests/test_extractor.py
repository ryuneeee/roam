import unittest
from ..detector.extractor import *


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
        self.assertEqual((6,), extract_seasons('The Vampire Diaries S06E09 720p HDTV x264-DIMENSION'))

    def test_episide(self):
        self.assertEqual((1,), extract_episode('E01'))
        self.assertEqual((1, 2, 3, ), extract_episode('E01-E03'))
        self.assertEqual((4, 5, ), extract_episode('E04-E05'))
        self.assertEqual((4, 5, ), extract_episode('Episode04-Episode05'))
        self.assertEqual((1,), extract_episode('Episode1'))
        self.assertEqual((4,), extract_episode('4화'))
        self.assertEqual((4,), extract_episode('4회'))
        self.assertEqual((9,), extract_episode('The Vampire Diaries S06E09 720p HDTV x264-DIMENSION'))

    def test_date(self):
        self.assertEqual(('140530', ), extract_date('불후의 명곡 E001~E196 2011 / 140530 / TV / KBS2 / 720p / H.264 / MKV'))
        self.assertEqual(('140530', '140531'), extract_date('140530~140531'))

    def test_year(self):
        self.assertEqual(('2011', ), extract_year('불후의 명곡 E001~E196 2011 / TV / KBS2 / 720p / H.264 / MKV'))

    def test_resolution(self):
        self.assertEqual(('SD', ), extract_resolution('The Vampire Diaries S06E09 SD HDTV x264-DIMENSION'))
        self.assertEqual(('720p', ), extract_resolution('The Vampire Diaries S06E09 720p HDTV x264-DIMENSION'))
        self.assertEqual(('1080p', ), extract_resolution('The Vampire Diaries S06E09 1080p HDTV x264-DIMENSION'))
        self.assertEqual(('1080i', ), extract_resolution('The Vampire Diaries S06E09 1080i HDTV x264-DIMENSION'))
        self.assertEqual(('4K', ), extract_resolution('The Vampire Diaries S06E09 4K HDTV x264-DIMENSION'))
        self.assertEqual((), extract_resolution('The Vampire Diaries S06E09 HDTV x264-DIMENSION'))

    def test_video_codec(self):
        self.assertEqual(('x264', ), extract_video_codec('The Vampire Diaries S06E09 720p HDTV x264-DIMENSION'))
        self.assertEqual(('h264', ), extract_video_codec('The Vampire Diaries S06E09 720p HDTV h264-DIMENSION'))

    def test_audio_codec(self):
        self.assertEqual(('AAC', ), extract_audio_codec('The Vampire Diaries S06E09 720p AAC HDTV x264-DIMENSION'))

    def test_source(self):
        self.assertEqual(('HDTV', ), extract_source('The Vampire Diaries S06E09 720p HDTV x264-DIMENSION'))
        self.assertEqual(('Blu-ray', ), extract_source('The Vampire Diaries S06E09 720p Blu-ray x264-DIMENSION'))
