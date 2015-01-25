__author__ = 'Ryun'

from glob import glob
import os

class TrackerManager():

    def get_lists(self):
        curdir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(curdir)

        trackers = glob('[!_]*.py')
        trackers.remove(os.path.basename(__file__))
        return trackers

    # TODO: Save trackers into dict after import python modules and make Tracker obj.
    # Import modules: https://github.com/storyhe/playWithBot/blob/master/slask.py#L31
    def load_all(self):
        trackers = self.get_lists()
        return trackers
