import unittest
from ..models.torrent import Torrent

__author__ = 'Ryun'

torrent_info = {
            'name': 'My Little Television',
            'subname': 'Special Episode',
            'link': 'fake.php?id=293592',
            'torrent_id': '293592',
            'season': 'S01',
            'episode': 'E04',
            'date': '150514',
            'year': '2015',
            'resolution': '720p',
            'source': 'HDTV',
            'video_codec': 'H.264',
            'audio_codec': 'AVC'
        }

class testTorrent(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def test_create_by_kwargs(self):
        t = Torrent(**torrent_info)

        for k, v in torrent_info.items():
            self.assertEqual(t.__getattribute__(k), v)

    def tearDown(self):
        super().tearDown()
