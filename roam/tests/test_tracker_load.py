__author__ = 'Ryun'

import os
import unittest
from ..trackers import manager

class testTracker(unittest.TestCase):

    def setUp(self):
        super().setUp()

        curdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/trackers'
        os.chdir(curdir)

        # Make dummy file
        open('dummy_tracker_one.py', 'a').close()
        open('dummy_tracker_two.py', 'a').close()

        # Create TrackerManager
        self.tmgr = manager.TrackerManager()


    def test_file_lists(self):
        list = self.tmgr.file_lists()
        self.assertIn('dummy_tracker_one.py', list)
        self.assertIn('dummy_tracker_two.py', list)


    def test_load_module(self):
        trackers = self.tmgr.load_trackers()
        self.assertIn('roam.trackers.dummy_tracker_one', trackers.keys())
        self.assertIn('roam.trackers.dummy_tracker_two', trackers.keys())

    def test_refresh_modules(self):
        trackers = self.tmgr.load_trackers()
        now_trackers_count = len(trackers)

        open('dummy_tracker_three.py', 'a').close()
        trackers = self.tmgr.refresh_trackers()

        self.assertEqual(now_trackers_count+1, len(trackers))
        os.remove('dummy_tracker_three.py')

    def tearDown(self):
        # Remove dummy file
        os.remove('dummy_tracker_one.py')
        os.remove('dummy_tracker_two.py')
        self.assertFalse(os.path.isfile('dummy_tracker_one.py'))
        self.assertFalse(os.path.isfile('dummy_tracker_two.py'))

        super().tearDown()