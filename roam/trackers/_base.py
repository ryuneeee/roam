from abc import abstractmethod
import os

__author__ = 'Ryun'

class Tracker():

    def __init__(self):
        super().__init__()
        self.name = os.path.splitext(os.path.basename(__file__))[0]

    @abstractmethod
    def login(self):
        """
        Login to tracker.
        :return: cookie store
        """
        raise NotImplementedError('Not implemented yet.')

    @abstractmethod
    def fetch(self):
        """
        Fetch to main page at tracker using cookie store
        :return: torrent tuple
        """
        raise NotImplementedError('Not implemented yet.')

    @abstractmethod
    def search(self, keyword):
        """
        Search torrent
        :return: torrent tuple
        """
        raise NotImplementedError('Not implemented yet.')