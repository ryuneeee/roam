import os
import sys
# append PYTHONPATH to roam's home dir
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

from trackers import manager
import unittest

__author__ = 'Ryun'


class testTracker(unittest.TestCase):

    def setUp(self):
        super().setUp()

        curdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/trackers'
        os.chdir(curdir)

        # Make dummy file
        open('dummy_tracker.py', 'a').close()
        open('dummy_tracker_two.py', 'a').close()

        # Create TrackerManager
        self.tmgr = manager.TrackerManager()


    def t1est_file_lists(self):
        list = self.tmgr.file_lists()
        self.assertIn('dummy_tracker.py', list)
        self.assertIn('dummy_tracker_two.py', list)


    def t1est_load_module(self):
        trackers = self.tmgr.load_trackers()
        self.assertIn('trackers.dummy_tracker', trackers.keys())
        self.assertIn('trackers.dummy_tracker_two', trackers.keys())

    def test_refresh_modules(self):
        trackers = self.tmgr.load_trackers()
        self.assertEqual(2, len(trackers))

        open('dummy_tracker_three.py', 'a').close()
        trackers = self.tmgr.refresh_trackers()

        self.assertEqual(3, len(trackers))
        print(trackers)
        os.remove('dummy_tracker_three.py')

    def tearDown(self):
        # Remove dummy file
        os.remove('dummy_tracker.py')
        os.remove('dummy_tracker_two.py')
        self.assertFalse(os.path.isfile('dummy_tracker.py'))
        self.assertFalse(os.path.isfile('dummy_tracker_two.py'))

        super().tearDown()

if __name__ == '__main__':
    unittest.main(verbosity=2)