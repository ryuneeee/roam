import http
import unittest
from ..trackers.manager import TrackerManager

__author__ = 'Ryun'


class testTracker(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.tmgr = TrackerManager()
        trackers = self.tmgr.load_trackers()
        for tracker in trackers.values():
            cj = tracker.login()
            self.assertIsInstance(cj, http.cookiejar.CookieJar)

    def tearDown(self):
        super().tearDown()