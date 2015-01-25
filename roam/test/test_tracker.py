import os
import unittest
from trackers import manager

__author__ = 'Ryun'


class testTracker(unittest.TestCase):

    def setUp(self):
        super().setUp()

    def test_get_lists(self):
        curdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/trackers'
        os.chdir(curdir)

        # Make dummy file
        open('dummy_tracker.py', 'a').close()

        tmgr = manager.TrackerManager()
        list = tmgr.get_lists()
        self.assertIn('dummy_tracker.py', list)

        # Remove dummy file
        os.remove('dummy_tracker.py')
        self.assertFalse(os.path.isfile('dummy_tracker.py'))


    def tearDown(self):
        super().tearDown()

if __name__ == '__main__':
    unittest.main(verbosity=2)