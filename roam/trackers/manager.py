import importlib

__author__ = 'Ryun'

from glob import glob
import os


class TrackerManager():

    def file_lists(self):
        curdir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(curdir)

        trackers = glob('[!_]*.py')
        trackers.remove(os.path.basename(__file__))
        return trackers

    # TODO: Save trackers into dict or array after import python modules and make Tracker obj.
    # Import modules: https://github.com/storyhe/playWithBot/blob/master/slask.py#L31
    def load_modules(self):
        trackers = self.file_lists()

        loaded = []

        for tracker in trackers:
            loaded.append(importlib.import_module('trackers.'+tracker[:-3]))

        return loaded
