import importlib

__author__ = 'Ryun'

from glob import glob
import os


class TrackerManager():

    def __init__(self):
        self.trackers = {}

    def file_lists(self):
        curdir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(curdir)

        try:
            files = glob('[!_]*.py')
            files.remove(os.path.basename(__file__))
        except:
            # TODO: IOError Logging
            raise IOError()

        return files

    def load_trackers(self):
        files = self.file_lists()

        for tracker in files:
            mod = importlib.import_module('trackers.%s' % tracker[:-3])
            self.trackers[mod.__name__] = mod

        return self.trackers

    def refresh_trackers(self):
        # Remove loaded module cache
        importlib.invalidate_caches()

        self.load_trackers()
        return self.trackers