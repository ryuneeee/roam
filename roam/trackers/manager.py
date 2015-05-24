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
            files.remove('base.py')
            files.remove(os.path.basename(__file__))
        except:
            # TODO: IOError Logging
            raise IOError()

        return files

    @staticmethod
    def instance_or_mod(mod):
        if len(dir(mod)) > 8:  # if not test or fake module, make tracker instance.
            cls = getattr(mod, dir(mod)[0])
            mod = cls()
        return mod

    def load_trackers(self):
        files = self.file_lists()

        for tracker in files:
            mod = importlib.import_module('roam.trackers.%s' % tracker[:-3])
            mod_name = mod.__name__
            mod = self.instance_or_mod(mod)
            self.trackers[mod_name] = mod

        return self.trackers

    def refresh_trackers(self):
        # Remove loaded module cache
        importlib.invalidate_caches()

        self.load_trackers()
        return self.trackers

    def login_trackers(self):
        for tracker in self.trackers.values():
            tracker.login()
