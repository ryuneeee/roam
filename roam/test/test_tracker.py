import os
import unittest
from trackers import manager

__author__ = 'Ryun'


class testTracker(unittest.TestCase):

    def setUp(self):
        super().setUp()

        curdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/trackers'
        os.chdir(curdir)

        # Make dummy file
        open('dummy_tracker.py', 'a').close()
        open('dummy_tracker_two.py', 'a').close()


    def test_file_lists(self):
        tmgr = manager.TrackerManager()
        list = tmgr.file_lists()
        self.assertIn('dummy_tracker.py', list)
        self.assertIn('dummy_tracker_two.py', list)


    def test_load_module(self):
        names = []

        tmgr = manager.TrackerManager()
        trackers = tmgr.load_modules()

        for tracker in trackers:
            names.append(tracker.__name__)

        self.assertIn('trackers.dummy_tracker', names)
        self.assertIn('trackers.dummy_tracker_two', names)



    def tearDown(self):
        # Remove dummy file
        os.remove('dummy_tracker.py')
        os.remove('dummy_tracker_two.py')
        self.assertFalse(os.path.isfile('dummy_tracker.py'))
        self.assertFalse(os.path.isfile('dummy_tracker_two.py'))

        super().tearDown()

if __name__ == '__main__':
    unittest.main(verbosity=2)